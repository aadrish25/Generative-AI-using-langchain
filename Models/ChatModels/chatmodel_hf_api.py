# huggingfaceendpoint is used when you want to use an API
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"E:\Generative-AI\.env")

# configure the llm you want to use first
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto"
)

# now pass the llm
model = ChatHuggingFace(llm=llm )

result = model.invoke("What is the capital of India?")

print(result.content)