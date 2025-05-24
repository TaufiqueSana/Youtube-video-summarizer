import streamlit as st
from summarizer import extract_video_id, get_transcript, generate_summary

st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube Video URL")

if url:
    with st.spinner("Extracting and summarizing..."):
        transcript = get_transcript(url)
        if transcript:
            summary = generate_summary(transcript)
            st.subheader("📄 Summary")
            st.write(summary)
        else:
            st.error("Failed to extract transcript or captions.")
