from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# create prompt template 1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)


# create prompt template 2
template2 = PromptTemplate(
    template="Summarize the following text in 5 lines. \n {text}",
    input_variables=["text"]
)

# create a parser object of StrOutputParser
parser = StrOutputParser()

# create a chain 
# parsers work best with chain
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"black hole"})
print(result)
