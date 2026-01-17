from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

# create loader object
loader = DirectoryLoader(
    path=r"Document_Loaders\DirectoryLoader\pdf_folder",
    glob="*.pdf",# means load all pdfs from the books folder
    loader_cls=PyPDFLoader
)

# docs = loader.lazy()

docs = loader.lazy_load()

# print(next(docs))

for doc in docs:
    print(doc.metadata) # every time a single Document is loaded into memory