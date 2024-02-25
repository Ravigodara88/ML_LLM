from langchain_core.prompts import ChatPromptTemplate
from LangChainAzureBase import llm
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

def search_joke(topic1, topic2):
    """
    Search for a joke based on two topics.

    Args:
        topic1 (str): The first topic.
        topic2 (str): The second topic.

    Returns:
        dict: A dictionary containing the joke information, including the setup, punchline, explanation, and fun quotient.

    Example:
        >>> search_joke("cats", "dogs")
        {
            "setup": "Why don't cats play poker in the wild?",
            "punchline": "Too many cheetahs!",
            "explanation": "The joke plays on the double meaning of 'cheetahs' - both the animal and the term for cheating in poker.",
            "fun_quotient": 8
        }
    """
    functions = [
        {
            "name": "joke",
            "description": "A joke",
            "parameters": {
                "type": "object",
                "properties": {
                    "setup": {"type": "string", "description": "The setup for the joke"},
                    "punchline": {
                        "type": "string",
                        "description": "The punchline for the joke",
                    },
                    "explanation": {"type": "string", "description": "Explain the joke to those who didn't get"},
                    "fun_quotient": {"type": "integer", "description": "On a scale of 1 to 10, how funny is this joke? (10 being most funny and 1 being least funny)"}
                },
                "required": ["setup", "punchline", "explanation", "fun_quotient"],
            },
        }
    ]
    prompt = ChatPromptTemplate.from_template("Tell me a dark humor joke about what is common between {topic1} and {topic2}")
    chain = prompt | llm.bind(function_call={"name": "joke"}, functions=functions) | JsonOutputFunctionsParser()
    res = chain.invoke({"topic1": topic1, "topic2": topic2})
    return res


daily_things = ["dog", "tv", "nail", "car", "phone", "tree", "coffee", "book", "chair", "food"]
daily_things_extended = [ "sun", "sky", "clouds", "traffic", "buildings", "people", "music"]
import random
import time

# Randomly select 2 items from each list
topics1 = random.sample(daily_things, 2)
topics2 = random.sample(daily_things_extended, 2)

# Pass the selected topics to search_joke function
for topic1, topic2 in zip(topics1, topics2):
    print(search_joke(topic1, topic2))
    time.sleep(1)
