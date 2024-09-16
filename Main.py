import base64
import io
from dotenv import load_dotenv
import streamlit as st
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import PyPDF2

load_dotenv()

# Configure Azure AI
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.getenv("OPENAI_GPT4o_API_KEY")),
)


# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


# Function to get GPT-4o response
def get_gpt4o_response(input, pdf_text, prompt):
    response = client.complete(
        messages=[
            SystemMessage(content=prompt),
            UserMessage(content=input),
            UserMessage(content=pdf_text),
        ],
        model="gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1,
    )
    return response.choices[0].message.content


st.set_page_config(
    page_title="ATS - Resume Application Tracking System", page_icon="📚"
)
st.title("📚 ATS - Resume Application Tracking System")

input_text = st.text_area("Enter the job description", height=200, key="input")
pdf_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if pdf_file is not None:
    st.write("Resume uploaded successfully")

submit1 = st.button("Tell me about the Resume")
submit2 = st.button("How can I improve my Skills")
submit3 = st.button("Match my Resume with the Job Description( Percentage Match) ")
submit4 = st.button("Missing keywords in my Resume")

input_prompt1 = """
You are an expert Technical Recruiter at a leading technology company, responsible for assessing candidates' resumes using an Applicant Tracking System (ATS). Your task is to evaluate the candidate's resume in relation to the provided job description. Specifically, focus on the following areas:
- Relevance of skills, experience, and qualifications to the job description.
- Identification of any gaps in technical skills or relevant experience.
- Analysis of how well the resume is tailored for ATS screening, with attention to keyword usage, formatting, and structure.
- Provide actionable feedback on improving the resume to increase its ATS compatibility and alignment with the job role.
Please offer a professional, ATS-friendly review that includes both strengths and areas for improvement.
"""

input_prompt2 = """
You are a seasoned career coach with extensive experience in technology hiring. Your task is to analyze the candidate's resume in the context of the provided job description and offer detailed, practical advice on improving their skills and career trajectory.
Focus on the following aspects:
- Identify specific skills, certifications, or experiences that are missing or underrepresented compared to the job requirements.
- Provide recommendations on upskilling, including relevant courses, certifications, or projects that would make the candidate more competitive.
- Highlight any transferable skills from other roles that could be better emphasized or framed in the resume.
- Advise on how to improve the overall presentation of the resume for ATS scanning.
Offer tailored, constructive feedback to help the candidate align more closely with the job requirements.
"""


input_prompt3 = """
You are a sophisticated ATS system that evaluates resumes against job descriptions to calculate their compatibility. Your task is to:
- Analyze the candidate's resume and compare it to the provided job description.
- Calculate the percentage match based on how closely the resume aligns with the required skills, qualifications, and experience listed in the job description.
- Highlight key strengths in the resume that match the job description.
- Identify missing or underrepresented keywords and skills that could improve the candidate's chances of being selected.
- Provide an overall assessment of how well the candidate fits the role, along with the final percentage match score.
Your evaluation should be detailed, data-driven, and clearly justify the match score.
"""


input_prompt4 = """
You are an advanced ATS system tasked with identifying gaps in resumes. Your role is to:
- Analyze the resume in detail, focusing on the job description and expected keywords.
- Identify important keywords, skills, and technical terms that are missing or insufficiently mentioned in the resume.
- Explain how these missing elements could impact the candidate's chances of passing ATS filters.
- Provide a list of critical missing keywords and suggest how they can be incorporated into the resume to improve its relevance and match to the job description.
Ensure that your feedback is thorough and actionable, aimed at increasing the resume's chances of being shortlisted.
"""

if submit1:
    if pdf_file is not None:
        pdf_text = extract_text_from_pdf(pdf_file)
        response = get_gpt4o_response(input_text, pdf_text, input_prompt1)
        st.subheader("Resume Review")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

if submit2:
    if pdf_file is not None:
        pdf_text = extract_text_from_pdf(pdf_file)
        response = get_gpt4o_response(input_text, pdf_text, input_prompt2)
        st.subheader("Resume Feedback")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

if submit3:
    if pdf_file is not None:
        pdf_text = extract_text_from_pdf(pdf_file)
        response = get_gpt4o_response(input_text, pdf_text, input_prompt3)
        st.subheader("Resume Match")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

if submit4:
    if pdf_file is not None:
        pdf_text = extract_text_from_pdf(pdf_file)
        response = get_gpt4o_response(input_text, pdf_text, input_prompt4)
        st.subheader("Missing Keywords")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
