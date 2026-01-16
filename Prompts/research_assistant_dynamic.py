from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import load_prompt

load_dotenv(dotenv_path=r"E:\Generative-AI\.env")

# define the llm you are going to use
llm = ChatGroq(model="llama-3.1-8b-instant",max_tokens=1000,temperature=0)

# define the application title
st.header("Research Assistant")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# load the prompt template
template = load_prompt(path=r"E:\Generative-AI\Prompts\template.json")




# send the prompt to the model if summarize button is clicked
if st.button("Summarize"):
    # create a chain of the two processes --> create a prompt and pass to model
    chain = template | llm
    
    # now you need to invoke only the chain
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    
    # and then display the result
    st.write(result.content)