# ATS - Resume Application Tracking System

This Streamlit application allows users to analyze resumes against job descriptions using Google's Generative AI model, Gemini. Users can upload a resume in PDF format and input a job description to receive various analyses.

## Installation

1. Install required packages by running the following commands:

   ```bash
   sudo apt-get update
   sudo apt-get install -y --no-install-recommends poppler-utils
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Load environment variables:

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

2. Configure Gemini API key:

   ```python
   genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
   ```

   Get your API key from [Google AI Studio ](https://aistudio.google.com/app/apikey)

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Functionality

- **Resume Review**: Analyze how well a resume aligns with a job description from a Technical HR Manager's perspective.
- **Resume Feedback**: Receive suggestions on improving skills and experience to match a job description from a Career Coach.
- **Resume Match**: Get a percentage match between a resume and a job description along with missing keywords from an ATS perspective.
- **Missing Keywords**: Identify keywords missing from a resume based on a job description.

## Inputs

- **Job Description**: Enter the job description.
- **Resume Upload**: Upload a resume in PDF format.

## Outputs

- **Resume Review**: Professional evaluation of resume alignment with the job description.
- **Resume Feedback**: Suggestions for improving skills and experience.
- **Resume Match**: Percentage match with job description and missing keywords.
- **Missing Keywords**: List of keywords missing from the resume.

## Deployment

The application is deployed on Streamlit and can be accessed [here](https://resume-track.streamlit.app/).

## About me

I am a Data Scientist with a passion for Natural Language Processing and Machine Learning. I am currently working on projects that involve text analysis and generation using state-of-the-art models.

## Note

This application is for educational purposes only and should not be used for commercial purposes.

For any issues or suggestions, please feel free to reach out to me at [Visesh Agarwal LinkedIn](https://www.linkedin.com/in/viseshagarwal/)
