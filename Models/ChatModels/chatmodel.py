from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv(dotenv_path="E:\Generative-AI\.env")

model = ChatGroq(model="openai/gpt-oss-120b",temperature=1.8)

result = model.invoke(input="Write 5 line rhyming poem on cricket.")

print(result.content)