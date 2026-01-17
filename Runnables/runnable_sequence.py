from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# create llm
llm = ChatGroq(model="openai/gpt-oss-20b")

# create prompt template
template = PromptTemplate(
    template="Write me a funny joke on {topic}",
    input_variables=["topic"]
)

# create parser
parser = StrOutputParser()

# create chain
chain = template | llm | parser

response = chain.invoke({'topic':'maths'})

print(response)