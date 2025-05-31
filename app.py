import streamlit as st
from resume_parser import extract_text_from_pdf
from review_chain import get_resume_feedback

st.title(" GenAI Resume Reviewer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text Preview")
    st.text_area("Resume Content", resume_text, height=300)

    if st.button(" Analyze Resume"):
        feedback = get_resume_feedback(resume_text)
        st.subheader(" AI Feedback")
        st.write(feedback)
