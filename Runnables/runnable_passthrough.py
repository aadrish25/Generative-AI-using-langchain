from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough

load_dotenv()

# create llm
llm = ChatGroq(model="llama-3.3-70b-versatile")

# prompt1
template1 = PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Explain the following joke: \n {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

# chain which generates joke
joke_generator = template1 | llm | parser

# paraller_chain which displays th joke and explain the joke
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': template2 | llm | parser
})

# merge the two chains
final_chain = joke_generator | parallel_chain

result = final_chain.invoke({'topic':'AI'})

print(result)