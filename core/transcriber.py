import whisper
import os
import requests

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "tiny")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

_model = None

def load_model():
    global _model
    if _model is None:
        print(f"Loading Whisper {WHISPER_MODEL} model...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("Whisper model loaded successfully")
    return _model

def transcribe_chunk_whisper(chunk_path : str) -> str:
    model = load_model()

    result = model.transcribe(chunk_path, task="transcribe")
    return result["text"].strip()

import requests
from pydub import AudioSegment
import tempfile
import os


def transcribe_chunk_sarvam(chunk_path: str) -> str:
    if not SARVAM_API_KEY:
        raise RuntimeError("SARVAM_API_KEY is not set")

    headers = {
        "api-subscription-key": SARVAM_API_KEY
    }

    audio = AudioSegment.from_wav(chunk_path)
    segment_ms = 25 * 1000

    transcripts = []

    for i, start in enumerate(range(0, len(audio), segment_ms)):

        segment = audio[start:start + segment_ms]
        temp_path = f"{chunk_path}_sarvam_{i}.wav"

        segment.export(temp_path, format="wav")

        try:
            with open(temp_path, "rb") as f:
                files = {
                    "file": (
                        os.path.basename(temp_path),
                        f,
                        "audio/wav"
                    )
                }

                data = {
                    "model": SARVAM_MODEL
                }

                response = requests.post(
                    SARVAM_STT_TRANSLATE_URL,
                    headers=headers,
                    files=files,
                    data=data,
                    timeout=300
                )

            response.raise_for_status()

            result = response.json()
            text = result.get("transcript", "")

            if text:
                transcripts.append(text.strip())

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    return " ".join(transcripts)

def transcribe_chunk(chunk_path : str, language : str = "english") -> str:
    """
       Route one chunk to Whisper or Sarvam depending on language choice.
       - english  → Whisper (local model)
       - hinglish → Sarvam (translates to English while transcribing)
       """

    if language.lower() == "hinglish":
        return transcribe_chunk_sarvam(chunk_path)
    return transcribe_chunk_whisper(chunk_path)

def transcribe_all(chunks: list, language : str = "english") -> str:
    full_transcript = ""

    engine = "Sarvam AI" if language.lower() == "hinglish" else "Whisper"
    print(f"Using {engine} for transcription...")

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}...")

        text = transcribe_chunk(chunk, language=language)

        full_transcript += text + " "

    print("Transcription completed!")

    return full_transcript.strip()

