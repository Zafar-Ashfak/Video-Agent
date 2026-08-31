import yt_dlp
import os

from pydub import AudioSegment

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        original_filename = ydl.prepare_filename(info)
        filename = os.path.splitext(original_filename)[0] + ".wav"

    return filename


url = "https://www.youtube.com/watch?v=0fB0gr_M7Pw"


print(download_youtube_audio(url))
data = download_youtube_audio(url)

def convert_to_wav(input_path : str) -> str:
    """ Convert any audio/video file to wav format using pydub. """
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) # 16khz
    audio.export(output_path, format="wav")
    return output_path

print(convert_to_wav(data))
