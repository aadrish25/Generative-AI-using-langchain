from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

template = PromptTemplate(
    template="Generate 5 interesting facts on {topic}",
    input_variables=["topic"],
)

chain = template | model | parser

result = chain.invoke({'topic':'Extra terrestrial life'})

# print(result)

# visualize chain
chain.get_graph().print_ascii()