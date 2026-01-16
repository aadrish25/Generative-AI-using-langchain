from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summarize the report
template2 = PromptTemplate(
    template="Write a 5 line summary on the following {text}.",
    input_variables=["text"]
)

# create the first prompt and send to model
prompt1 = template1.invoke({'topic':'black holes'})

# get the response from the model
response1 = model.invoke(prompt1)

# with the response1, create prompt2
prompt2 = template2.invoke({'text':response1.content})

# get the response of the model for prompt 2
response2 = model.invoke(prompt2)

print(response2.content)