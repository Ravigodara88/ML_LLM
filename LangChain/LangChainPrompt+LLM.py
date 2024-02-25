from langchain_core.prompts import ChatPromptTemplate
from LangChainAzureBase import llm

def search_joke(topic1, topic2):
    """
    This function searches for a joke related to two given topics using LangChain chaining prompt and LLM.

    Args:
        topic1 (str): The first topic.
        topic2 (str): The second topic.

    Returns:
        str: The joke related to the given topics.
    """
    prompt = ChatPromptTemplate.from_template("Tell me a joke about following What is common between {topic1} and {topic2}")
    chain = prompt | llm
    res = chain.invoke({"topic1":topic1,"topic2":topic2})
    return res

print(search_joke("cats", "dogs"))
