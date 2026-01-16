from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# keep a track of chat history
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input("You: ")
    
    # append the current user_input to chat_history, after converting into HumanMessage
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == 'exit':
        break
    
    # instead of sending a single prompt, send the entire chat history to model
    result = model.invoke(chat_history)
    
    # also append the current model response to chat_history, after converting into AIMessage
    chat_history.append(AIMessage(content=result.content))
    
    print(f"AI : {result.content}")