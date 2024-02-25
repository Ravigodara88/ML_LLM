from LangChainAzureBase import llm
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Tell me a joke about following What is common betweent {topic1} and {topic2}")
chain = prompt | llm
res =   llm.invoke(input("Enter the query to search: "))
print(res)
