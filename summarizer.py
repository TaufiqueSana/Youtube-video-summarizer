import re
import os
import whisper
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

# Load Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def get_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript])
    except:
        return None

def download_audio(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    output_path = stream.download(filename="audio.mp4")
    return output_path

def get_audio_transcript(video_url):
    model = whisper.load_model("base")
    audio_file = download_audio(video_url)
    result = model.transcribe(audio_file)
    os.remove(audio_file)  # optional cleanup
    return result["text"]

def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        return None
    text = get_captions(video_id)
    if text:
        return text
    return get_audio_transcript(url)

def split_text(text, max_words=500):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

def generate_summary(text):
    chunks = split_text(text)
    summaries = [summarizer(chunk)[0]["summary_text"] for chunk in chunks]
    return "\n\n".join(summaries)
