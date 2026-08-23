## YouTube Video Transcript Summarizer using Generative AI


### Introduction
This project is a Generative AI-powered web application that summarizes YouTube videos using their available transcripts. Users can provide a YouTube video link and select the transcript language, after which the application extracts the transcript and generates concise detailed notes using Google Gemini. Built with Streamlit, the application provides a simple and interactive interface for converting lengthy video transcripts into easy-to-read summaries.


### Technologies Used
* Python
* Google Gemini
* YouTube Transcript API
* Streamlit


### Installation

#### Clone the Repository

```bash
git clone https://github.com/archna13/YouTube-Video-Transcript-Summarizer-using-Generative-AI.git
````

#### Create a Virtual Environment

```bash
python -m venv .venv
```

#### Activate the Environment

```bash
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the project root directory.

```env
GOOGLE_API_KEY=your_google_api_key
```

#### Run the Application

```bash
streamlit run app.py
```


### Features

* **YouTube Video Input:** Users can enter a YouTube video URL through the Streamlit sidebar. The application extracts the video ID from the provided URL and displays the corresponding YouTube thumbnail.

* **Multi-Language Transcript Selection:** Users can select the required transcript language from the available language options, including English, Spanish, French, German, Chinese, Russian, Arabic, Hindi, and Tamil.

* **Transcript Extraction:** The application uses `YouTubeTranscriptApi` to retrieve the transcript associated with the selected YouTube video and language. The individual transcript segments are combined into a single text input for summarization.

* **Generative AI Summarization:** The extracted transcript is passed to Google Gemini with a predefined summarization prompt. The model generates concise notes containing the important points from the video within the specified response length.

* **Interactive Streamlit Interface:** Streamlit provides the user interface for entering the video URL, selecting the transcript language, triggering the summarization process, and displaying the generated notes.

* **Error Handling & User Feedback:** The application provides status messages while extracting transcripts and generating summaries. It also displays appropriate error messages when a transcript cannot be retrieved or a valid video URL is not provided.


### Conclusion

This project use to transform YouTube video transcripts into concise and useful notes using Generative AI. By combining transcript extraction with Google Gemini and an interactive Streamlit interface, the application makes lengthy video content easier to understand and review. It demonstrates a practical application of Generative AI for automated content summarization.
