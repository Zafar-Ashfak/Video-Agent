from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import textwrap
from dotenv import load_dotenv

load_dotenv()

source = "https://youtu.be/7Nyjm8IN708"
language = "hinglish"

chunks = process_input(source)
transcript = transcribe_all(chunks, language=language)

print("\nTranscription:\n")

print(textwrap.fill(transcript, width=100))