from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# create template1
template1 = PromptTemplate(
    template="Write me a detailed report on {topic}",
    input_variables=["topic"]
)

# create template2
template2 = PromptTemplate(
    template="Summarize the following text in 5 points: \n {text}",
    input_variables=["text"]
)

# create a parser
parser = StrOutputParser()

# create a chain
sequential_chain = template1 | model | parser | template2 | model | parser

response = sequential_chain.invoke({'topic':'Electric transformers'})

# print(response)

# visualize chain
sequential_chain.get_graph().print_ascii()