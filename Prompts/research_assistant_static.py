from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st 

load_dotenv(dotenv_path=r"E:\Generative-AI\.env")

# define the llm you are going to use
llm = ChatGroq(model="llama-3.1-8b-instant",max_tokens=1000,temperature=0)

# define the application title
st.header("Research Assistant")

# take the user input (prompt)
user_input = st.text_input("Enter your prompt")

# send the prompt to the model if summarize button is clicked
if st.button("Summarize"):
    result = llm.invoke(user_input)
    
    # and then display the result
    st.write(result.content)