from audio_downloader import download_audio
from transcriber import transcribe_audio
from llm_client import summarize_text

if __name__ == "__main__":
    download_audio()
    transcribe_audio()
    summarize_text()
