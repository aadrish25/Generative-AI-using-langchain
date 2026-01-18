from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter


# create a document loader
doc_loader = PyPDFLoader(file_path=r"Text_Splitters\LengthBased\chapter_4.pdf")

doc = doc_loader.load()
# print(doc)

# text-splitter
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
    separator=''
)

# split document
doc_split = splitter.split_documents(doc) # each chunk stored as a document object

print(doc_split[0].page_content)