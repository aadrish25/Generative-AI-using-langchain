from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# create a Pydantic object, which will act as schema
class Person(BaseModel):
    name : str = Field(description="Name of the person")
    age : int = Field(description="Age of the person",gt=18)
    city : str = Field(description="Name of the city the person lives in.")
    
# create the parser
pydantic_parser = PydanticOutputParser(pydantic_object=Person)

# create the prompt now
template = PromptTemplate(
    template="Give me the name, age and city of a character from {media_name}. \n {format_instruction}",
    input_variables=["media_name"],
    partial_variables={'format_instruction':pydantic_parser.get_format_instructions()}
)

# create a chain 
chain = template | model | pydantic_parser

result = chain.invoke({'media_name':'The Big Bang Theory'})

print(result)

