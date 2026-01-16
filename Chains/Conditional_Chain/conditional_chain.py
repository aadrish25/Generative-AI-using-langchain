from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

# restrict the sentiment the llm predicts to be strictly positive or negative
class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Classify the sentiment of the feedback")
    
# create pydantic parser
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# create prompts
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback as positive or negative: \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


prompt2 = PromptTemplate(
    template="Create an appropriate response for the following positive feedback : \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Create an appropriate response for the following negative feedback : \n {feedback}",
    input_variables=["feedback"]
)

# create classifier chain which classifies the feedback
classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke({'feedback':'This was a terrible product'}))

# create the conditional chain, using RunnableBranch
conditional_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find a sentiment.")
)

# merge the classifier and conditional chain

final_chain = classifier_chain | conditional_chain

response = final_chain.invoke({'feedback':"This is a terrible product."})

# print(response)

# visualize graph
final_chain.get_graph().print_ascii()