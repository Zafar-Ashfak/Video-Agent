from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://youtu.be/Ty8gcCKuwNI"

chunks = process_input(source)

transcript = transcribe_all(chunks)

print("\nFinal Transcript:\n")
print(transcript)