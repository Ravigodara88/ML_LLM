from LangChainAzureBase import llm

def zero_shot_prompt():
    """
    This function demonstrates the usage of zero-shot prompt in LangChain.
    It prompts the user to enter a query and invokes the LangChain model to search for relevant information.
    The result is then printed to the console.
    """
    res = llm.invoke(input("Enter the query to search: "))
    print(res)

zero_shot_prompt()
