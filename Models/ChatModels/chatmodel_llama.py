from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(dotenv_path="E:\Generative-AI\.env")

model = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

result = model.invoke("What do you know about Spiderman?")

print(result.content)