

# GenAI Resume Reviewer

A Generative AI-powered resume feedback tool that reads uploaded PDFs and provides professional, structured feedback using an LLM via LangChain.

---

## Features

-  Upload a resume (PDF)
- Get LLM-generated feedback on:
  - Skills  
  - ATS friendliness  
  - Project quality  
  - Areas to improve  
- Simple web UI via Streamlit
- Works offline with Ollama + Mistral model

---

##  Tech Stack

- **Python**
- **LangChain**
- **Ollama** (`mistral` model)
- **Streamlit**
- **PyMuPDF** (for PDF parsing)
- **WSL (Ubuntu)**

---

## Folder Structure

genai-app/
│
├── app.py # Streamlit UI
├── resume_parser.py # Extracts text from PDF
├── review_chain.py # Sends prompt to LLM and receives response
├── prompts/
│ └── feedback_prompt.txt # Prompt template
├── README.md # ← You are here
└── newenv/ # (your Python virtual environment)



---

## How to Run (WSL Ubuntu)

### 1. Start Ollama (in one terminal):

ollama serve
2. In another WSL terminal:

cd /mnt/c/Users/DELL/Desktop/genai\ app
source newenv/bin/activate
streamlit run app.py
Then open: http://localhost:8501

 Works only if mistral model is already pulled:


ollama run mistral
 Sample Output
Input Resume:

Aswathi V K  
Backend Developer | Java, Spring Boot, Docker  
Built REST APIs secured with JWT Auth.  
Deployed on AWS EC2 with MySQL, Docker  
Output:


 Good use of backend tech stack  
 Add quantifiable achievements  
 Expand on project impact  
 ATS friendly format
 Requirements

pip install streamlit langchain langchain-community pymupdf
 Model Details
This app uses the Mistral model served locally via Ollama:


ollama run mistral
If not already installed:


ollama pull mistral
Author
Aswathi V K
Site24x7 Intern | Python + Spring Boot + GenAI Enthusiast
LinkedIn

License
MIT License



