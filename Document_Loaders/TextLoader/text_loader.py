from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# create llm
llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template="Summarize this text in 100 words: \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# create a TextLoader object, pass the file path, and encoding type
loader = TextLoader(file_path=r"Document_Loaders\TextLoader\black_holes.txt",autodetect_encoding=True)

# load the text file, using load method
doc = loader.load()

# create chain
chain = prompt | llm | parser

response = chain.invoke({'text':doc[0].page_content})

print(response)