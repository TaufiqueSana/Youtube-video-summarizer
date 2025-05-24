# YouTube Video Summarizer

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-green)](https://youtube-video-summarizer-zuhkczrfy3stxzl2wkbovc.streamlit.app/)

A Streamlit web application that extracts transcripts from YouTube videos and generates concise summaries using state-of-the-art NLP models like Whisper and BART.

---

## 🚀 Live Demo

Try the app live here:  
👉 [YouTube Video Summarizer](https://youtube-video-summarizer-zuhkczrfy3stxzl2wkbovc.streamlit.app/)

---

## Features

- Extracts video captions using YouTube Transcript API if available
- Uses OpenAI Whisper model as fallback for audio transcription
- Summarizes long transcripts using Hugging Face's BART summarization model
- Handles long texts by chunking for better summarization results
- Simple and user-friendly Streamlit interface

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Youtube_summarizer.git
    cd Youtube_summarizer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Make sure `ffmpeg` is installed and added to your system PATH.  
   [FFmpeg Installation Guide](https://ffmpeg.org/download.html)

---

## Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```
## Project Structure
```bash
Youtube_summarizer/
├── app.py               # Main Streamlit app
├── summarizer.py        # Functions for transcript extraction & summarization
├── requirements.txt     # Project dependencies
├── README.md            # This file
└── venv/                # Virtual environment (excluded from repo)
```

## Notes

The first time you run the app, Whisper model weights (~1.6GB for the base model) will be downloaded.
The app requires internet connection to access YouTube transcripts and models.

**Important:** The app does **not** work properly with YouTube Shorts or live videos, as these formats often lack standard transcripts or have streaming constraints.

## License

This project is licensed under the MIT License.

## Contact

For any queries or suggestions, please contact:

Username : TaufiqueSana   
Email: taufiquesana171@gmail.com
