from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import textwrap

source = "https://youtu.be/ZELPNFXJ4_o"

chunks = process_input(source)

transcript = transcribe_all(chunks)

print("\nTranscription:\n")

print(textwrap.fill(transcript, width=100))