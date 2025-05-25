import streamlit as st
from summarizer import extract_video_id, get_transcript, generate_summary

# Page configuration
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="centered"
)

# Background image using Streamlit's HTML and CSS
st.markdown(
    """
    <style>

    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-top: 2rem;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 12px;
        font-size: 1rem;
    }
    .stButton > button {
        border-radius: 8px;
        background-color: #1E90FF;
        color: white;
        padding: 12px 28px;
        border: none;
        font-weight: bold;
        font-size: 1rem;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #cc0000;
    }
    .summary-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-size: 1.05rem;
        color: #333333;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Title and input
st.markdown("<h1 style='text-align: center; color: #1E90FF;'>🎥 YouTube Video Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>Summarize YouTube video into concise text with just one click.</p>", unsafe_allow_html=True)
st.markdown("----")

# Input field
st.markdown("#### 🔗 **Enter YouTube Video URL**")
url = st.text_input("", label_visibility="collapsed")

# Button
generate = st.button("✨ Generate Summary")

# Logic
if generate and url:
    with st.spinner("⏳ Extracting transcript and generating summary..."):
        transcript = get_transcript(url)
        if transcript:
            summary = generate_summary(transcript)
            st.success("✅ Summary generated successfully!")
            st.markdown("### 📄 Summary")
            st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)
        else:
            st.error("❌ Failed to extract transcript or captions. Please try a different video.")
elif generate and not url:
    st.warning("⚠️ Please enter a valid YouTube URL before clicking the button.")  