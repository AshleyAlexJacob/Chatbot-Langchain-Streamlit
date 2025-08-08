import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv(".env")

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 2,
    max_output_tokens = 1024,
    timeout=None,
    max_retries=2,
)

st.title("Custom Chatbot")

user_message =  st.chat_input("Enter your message:")
st.chat_message("user").write(user_message)
if user_message:
    messages = [
        {
            "role": "user",
            "content": user_message,
        }
    ]
    
    response = llm.invoke(messages)
    
    st.chat_message("assistant").write(response.content)
    