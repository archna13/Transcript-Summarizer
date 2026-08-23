import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure the Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the base prompt for the AI model
base_prompt = """You are a YouTube video summarizer. You will be taking the transcript text in {} and summarizing the entire video, 
providing the important points in a concise manner (within 500 words). 
Please provide the summary of the text given here: """

# Function to extract transcript details from a YouTube video
def extract_transcript_details(youtube_video_url, language="en"):
    try:
        video_id = youtube_video_url.split("v=")[1]
        # Fetch transcript in the selected language
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

# Function to generate the summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# Custom CSS to center the title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered Title
st.markdown('<div class="title">YouTube Video Transcript Summarizer</div>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    # Input for YouTube link
    youtube_link = st.text_input("Enter YouTube Video Link:")

    # Language selection dropdown
    language = st.selectbox("Select Transcript Language", ["en", "es", "fr", "de", "zh", "ru", "ar", "hi","ta"], index=0)

if youtube_link:
    # Display YouTube thumbnail
    video_id = youtube_link.split("v=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True, caption="YouTube Thumbnail")

# Button to get the transcript and summary
if st.sidebar.button("Get Detailed Notes"):
    if youtube_link:
        # Extract transcript in the selected language
        with st.spinner(f"Extracting transcript in {language}..."):
            transcript_text = extract_transcript_details(youtube_link, language)

        if transcript_text:
            st.success("Transcript extracted successfully!")
            
            # Adjust prompt based on language
            prompt = base_prompt.format(language)

            # Generate summary
            with st.spinner("Generating summary..."):
                summary = generate_gemini_content(transcript_text, prompt)
            
            if summary:
                st.markdown("## Detailed Notes:")
                st.write(summary)
        else:
            st.error(f"Could not extract transcript in {language}. Please check if the video supports this language.")
    else:
        st.error("Please enter a valid YouTube video link.")
