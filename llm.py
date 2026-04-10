from langchain.llms import OpenAI


def get_llm():
    return OpenAI(temperature=0)
