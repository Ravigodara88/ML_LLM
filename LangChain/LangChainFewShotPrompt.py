from LangChainAzureBase import llm

def chatbot_interaction():
    """
    Performs a few-shot prompting example using LangChain.

    This function demonstrates a conversation between a user and an assistant chatbot.
    The assistant uses the LangChain model to generate responses based on the user's input.

    The conversation is defined by a list of messages, where each message has a role (either "user" or "assistant")
    and content (the text of the message).

    Example:
        messages = [
            {"role": "user", "content": "Hi, how are you?"},
            {"role": "assistant", "content": "I am doing absolutely amazing! How are you?"},
            {"role": "user", "content": "I am doing well, thanks!"}
        ]

    Args:
        None

    Returns:
        None
    """

    chain = llm

    messages = [
        {"role": "system", "content": "You are a chatbot. You will only respond in the same tone the question was asked"},
        {"role": "user", "content": "Hi, how are you?"},
        {"role": "assistant", "content": "I am doing absolutely amazing! How are you?"},
        {"role": "user", "content": "I am doing well, thanks!"},
        {"role": "assistant", "content": "That's great to hear!"},
        {"role": "user", "content": "I am not doing well."},
        {"role": "assistant", "content": "Oh, sorry to hear that. Get well soon!"},
        {"role": "user", "content": "I am bad"},
        {"role": "assistant", "content": "Then I am your Dad"},
        {"role": "user", "content": "Enter the query to respond: I have a question."},  # Modified line
    ]

    res = chain.invoke(messages)
    print(res)

chatbot_interaction()
