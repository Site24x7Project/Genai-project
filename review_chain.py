from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# ✅ Use localhost
llm = Ollama(model="mistral", base_url="http://127.0.0.1:11434")

def get_resume_feedback(resume_text):
    prompt_template = """
You are a professional resume reviewer.
Given the resume below, give specific, honest feedback on:
- Skills
- ATS friendliness
- Project quality
- Areas to improve

Resume:
{resume}
    """
    prompt = PromptTemplate(input_variables=["resume"], template=prompt_template)
    chain_input = {"resume": resume_text}
    final_prompt = prompt.format(**chain_input)

    # 👇 DEBUG PRINT – shows what is sent to the model
    print("========== PROMPT SENT TO LLM ==========")
    print(final_prompt)
    print("========================================")

    response = llm.invoke(final_prompt)
    return response
