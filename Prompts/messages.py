from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# initialize the messages ( the chat history)
# telling the model to behave like a helpful assistant
# and then passing a human message 
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain")
]

# pass this messages to the model
result = model.invoke(messages)

# append the response of the model as an AIMessage to the chat history
messages.append(AIMessage(content=result.content))

print(messages)