from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# create a schema
schema = [
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic"),
]

# create the parser
parser = StructuredOutputParser.from_response_schemas(schema)

# create the prompt template
template = PromptTemplate(
    template="Provide me 3 facts on {topic}  \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# create the chain
chain = template | model | parser

# get chain output
result = chain.invoke({'topic':'black hole'})


print(result)