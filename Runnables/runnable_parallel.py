from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# create llm1
llm_x = ChatGroq(model="openai/gpt-oss-20b")

# create llm2
llm_linkedin = ChatGroq(model="llama-3.3-70b-versatile")

# create prompt1
template_x = PromptTemplate(
    template="Write a structured short X post on {topic}",
    input_variables=["topic"]
)

template_li = PromptTemplate(
    template="Write a structured short LinkedIn post on {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

# create runnable parallel
parallel_chain = RunnableParallel({
    'X': template_x | llm_x | parser,
    'LinkedIn':template_li | llm_linkedin | parser
})

print(parallel_chain.invoke({'topic':'AI'}))
