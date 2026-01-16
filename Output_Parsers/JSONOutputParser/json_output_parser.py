from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile",temperature=1.4)

json_parser = JsonOutputParser()

# create a prompt
template = PromptTemplate(
    template='Give me the name,age and city of a fictional character \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':json_parser.get_format_instructions()}
)

prompt = template.invoke({})

result = model.invoke(prompt)

# parse the model result
json_result = json_parser.parse(result.content)

print(json_result)