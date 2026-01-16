from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# now form a chat template, here the format is a little bit different
chat_template = ChatPromptTemplate([
    ("system","You a helpful {domain} expert."),
    ("human","Explain in simple terms, what is {topic}")
])

# now create the prompt
prompt = chat_template.invoke({
    'domain':'cricket',
    'topic':'yorker'
})

print(prompt)