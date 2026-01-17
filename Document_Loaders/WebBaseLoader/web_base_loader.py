from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template="Answer the question: {question} from the text : \n {text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()

# loader
loader = WebBaseLoader(web_path="https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDKTQZ/ref=sr_1_1_sspa?crid=3QL7GOIKW2CKO&dib=eyJ2IjoiMSJ9.VZ_alNzkt8TbfpXEQ6aSoxC0zkWM4esZ9IQhAM_RZRPUaekUrfaO2hO8ZPvDZIAq5VVpeZJjuyrhrwOmN5Ap61jadWN0aDtvdBGWLxBbtlLiQx_5e_LMAAQRlV2MDQb-at5Ews0N3081w6vsO5mu-0uiQ-_j365KaIOBr1OKi8SozrAY7wtX8QW_y5eTiv1o6Mmmd_oisCx38dU8cpcn5NcNBeXtiF4bgnpKLIWVZOk._zH47vPS2Kj8OYzKk2FfW2DsoxHSDh75WV-Hrqn-2uQ&dib_tag=se&keywords=laptop&qid=1768668247&sprefix=laptop%2Caps%2C380&sr=8-1-spons&aref=zsKjVxuqwq&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

docs = loader.load()

chain = prompt | llm | parser

response = chain.invoke({'question':'What is the specified storage?','text':docs[0].page_content})

print(response)