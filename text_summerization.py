from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables from .env file
load_dotenv()    # This will load the GROQ_API_KEY from the .env file into the environment variables -->GROQ_API_KEY = "gskxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"



llm_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

import streamlit as st

st.title("Text Summarization App")  
st.write("Enter text below to get a summary using Llama LLM.")

text_input = st.text_area("Enter a text to summarize:")   # user input text area

if st.button("Summarize"):
    prompt = f"summarize this text: {text_input}"
    response = llm_client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    st.write("Summary:", response.choices[0].message.content)
