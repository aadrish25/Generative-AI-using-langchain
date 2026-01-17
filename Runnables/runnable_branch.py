from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnablePassthrough

load_dotenv()

# create llm
llm = ChatGroq(model="openai/gpt-oss-20b")

# prompt
prompt = PromptTemplate(
    template="Generate a summary on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text within 500 words : \n {text}",
    input_variables=["text"]
)

# parser 
parser = StrOutputParser()

# chain generating summary
summary_gen_chain = prompt | llm | parser

# conditional summary
# if summary > 500 words, generate again
# else display summary
conditional_chain = RunnableBranch(
    (lambda x : len(x.split()) > 500, prompt2 | llm | parser),
    (lambda x : len(x.split()) <= 500, RunnablePassthrough()),
    RunnableLambda(lambda x : "No summary found")
)

# join the two chains
final_chain = summary_gen_chain | conditional_chain

response = final_chain.invoke({'topic':'Pollution in India'})
print(response)
