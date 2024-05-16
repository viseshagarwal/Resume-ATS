import base64
import io
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import os


# def install_packages():
# os.system("apt-get update")
# os.system("apt-get install -y --no-install-recommends poppler-utils")


# install_packages()


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_respose(input, pdf_content, prompt):
    model_name="gemini-1.5-flash-latest"
    model = genai.GenerativeModel(model_name)
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def get_pdf_content(pdf_file):
    if pdf_file is not None:
        images = pdf2image.convert_from_bytes(pdf_file.read())

        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode("utf-8"),
            }
        ]
        return pdf_parts
    else:
        raise Exception("Invalid file format. Please upload a PDF file.")


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
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt2 = """
You are a professional career coach, your task is to provide feedback on the resume.
Please provide suggestions on how the candidate can improve their skills and experience to better align with the job description.
"""
input_prompt4 = """
You are an experienced ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description.
Please provide a list of keywords that are missing from the resume.
"""

if submit1:
    if pdf_file is not None:
        pdf_content = get_pdf_content(pdf_file)
        response = get_gemini_respose(input_prompt1, pdf_content, input_text)
        st.subheader("Resume Review")
        st.write(response)

    else:
        st.write("Please upload a PDF file")


if submit2:
    if pdf_file is not None:
        pdf_content = get_pdf_content(pdf_file)
        response = get_gemini_respose(input_prompt2, pdf_content, input_text)
        st.subheader("Resume Feedback")
        st.write(response)
    else:
        st.write("Please upload a PDF file")


if submit3:
    if pdf_file is not None:
        pdf_content = get_pdf_content(pdf_file)
        response = get_gemini_respose(input_prompt3, pdf_content, input_text)
        st.subheader("Resume Match")
        st.write(response)
    else:
        st.write("Please upload a PDF file")


if submit4:
    if pdf_file is not None:
        pdf_content = get_pdf_content(pdf_file)
        response = get_gemini_respose(input_prompt4, pdf_content, input_text)
        st.subheader("Missing Keywords")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
