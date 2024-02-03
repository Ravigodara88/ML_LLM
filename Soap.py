from langchain_community.document_loaders import WebBaseLoader
import Google as Google
query =  input("Enter Subject to search:")
top_links = Google.get_top_links(query,3)

loader = WebBaseLoader(top_links)
import os
from langchain_openai import AzureChatOpenAI

docs = loader.load()
os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "AZURE_OPENAI_ENDPOINT"
from langchain_openai import AzureOpenAIEmbeddings
os.environ["OPENAI_API_KEY"] = "AZURE_OPENAI_KEY"
llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="gpt-4",
)
embeddings = AzureOpenAIEmbeddings(    openai_api_version="2023-05-15",
)
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")
document_chain = create_stuff_documents_chain(llm, prompt)



# from langchain_core.documents import Document

# with open("kaveri.txt", "r") as file:
#     content = file.read()
# document_chain = create_stuff_documents_chain(llm, prompt)
# response = document_chain.invoke({
#     "input": "Find BEMS related to  provisioning",
#     "context": [Document(page_content=content)]
# })

# print(response)

from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": input("Ask about your query ")+query})
print(response["answer"])