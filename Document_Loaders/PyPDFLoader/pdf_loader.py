from langchain_community.document_loaders import PyPDFLoader

# create an instance
loader = PyPDFLoader(file_path=r"Document_Loaders\PyPDFLoader\pdf_test.pdf")

# load the pdf
doc = loader.load()

# print(doc)

# print each page_content
for i,page in enumerate(doc):
    print(f"Page {i+1}")
    print(page.page_content)