# integration package between langchain and Groq
from langchain_groq import ChatGroq
# import the dotenv package which will load environment variables
from dotenv import load_dotenv

# load the API key
load_dotenv(dotenv_path="E:\Generative-AI\.env")

# create an Groq object, and specify the model you want to use
llm = ChatGroq(model="llama-3.1-8b-instant")

# call the invoke method
# the invoke method sends a prompt to the model
# the model processes the prompt, generates a reply and sends back
# we store the reply in a variable
result = llm.invoke(input="Who is Donald Trump?")

print(result.content)