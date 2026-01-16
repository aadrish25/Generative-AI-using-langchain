from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="llama-3.1-8b-instant")

model2 = ChatGroq(model="openai/gpt-oss-20b")

# create prompts
prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text : \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 10 short question answers from the following text : \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the following notes and quiz into a single document : \n notes --> {notes} \n quiz --> {quiz}",
    input_variables=["notes","quiz"]
)

# create a parser instance
parser = StrOutputParser()

# with RunnableParallel , you can execute multiple parallels at the same time
parallel_chain = RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

# create the chain to merge the notes and quiz
merger_chain = prompt3 | model1 | parser

# join the two chains, using a third chain
final_chain = parallel_chain | merger_chain

# this is the document
text = """ Chemical energy stored by molecules can be released as
heat during chemical reactions when a fuel like methane,
cooking gas or coal burns in air. The chemical energy may
also be used to do mechanical work when a fuel burns
in an engine or to provide electrical energy through a
galvanic cell like dry cell. Thus, various forms of energy
are interrelated and under certain conditions, these may
be transformed from one form into another. The study
of these energy transformations forms the subject matter
of thermodynamics. The laws of thermodynamics deal
with energy changes of macroscopic systems involving
a large number of molecules rather than microscopic
systems containing a few molecules. Thermodynamics is
not concerned about how and at what rate these energy
transformations are carried out, but is based on initial and
final states of a system undergoing the change. Laws of
thermodynamics apply only when a system is in equilibrium
or moves from one equilibrium state to another equilibrium
state. Macroscopic properties like pressure and temperature
do not change with time for a system in equilibrium state.
In this unit, we would like to answer some of the important
questions through thermodynamics, like:
How do we determine the energy changes involved in a
chemical reaction/process? Will it occur or not?
What drives a chemical reaction/process?
To what extent do the chemical reactions proceed?"""

# invoke the chain
result = final_chain.invoke({'text':text})

# print(result)

# visualize chain
final_chain.get_graph().print_ascii()

