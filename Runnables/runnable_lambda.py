from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnablePassthrough

load_dotenv()


# create llm
llm = ChatGroq(model="llama-3.3-70b-versatile")

# create prompt
prompt = PromptTemplate(
    template="Write a summary on {topic} under 100 words.",
    input_variables=["topic"]
)

parser = StrOutputParser()

# function which counts no of words
def count_words(text):
    return len(text.split())

# create chain which creates summary
summary_chain = prompt | llm | parser

# create parallel chain
parallel_chain = RunnableParallel({
    'Summary': RunnablePassthrough(),
    'Word Count': RunnableLambda(count_words)
})

# join the two chains
final_chain = summary_chain | parallel_chain

response = final_chain.invoke({
    'topic':'Pollution in India'
})

print(response)