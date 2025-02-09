import os
from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_fireworks import ChatFireworks


def get_model(model_name: str):
    """
    Gets the appropriate LangChain model based on the provided name.
    """
    match model_name:
        case "gpt-4o":
            return ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        case "gpt-4o-mini":
            return ChatOpenAI(model_name="gpt-4o", temperature=0.5, max_tokens=512)
        case "gpt3-mini":
            return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, max_tokens=512)
        case "gemini-flash-2.0":
            return ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.6, convert_system_message_to_human=True)
        case "claude-3.5-haiku":
            return ChatAnthropic(model_name="claude-3-haiku-20240307", temperature=0.6)
        case "llama-3.3-70b":
            return ChatFireworks(model_name="accounts/fireworks/models/llama-v3-70b-instruct", temperature=0.7)
        case _:
            raise ValueError(f"Unsupported model: {model_name}")


def generate_response(model_name: str, user_query: str) -> str:
    """
    Generates a response from the selected LLM based on the user query.

    Args:
        model_name: The name of the model to use (e.g., "gpt-4o", "claude-3-haiku").
        user_query: The user's question or input as a string.

    Returns:
        The LLM's response as a string.
    """
    try:
        model = get_model(model_name)
    except ValueError as e:
        return str(e)  # Return the error message if the model is invalid

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful chatbot."),
        ("user", "{input}")
    ])
    output_parser = StrOutputParser()

    chain = (
        {"input": RunnablePassthrough()}  # Pass the input through
        | prompt
        | model
        | output_parser
    )
    
    response = chain.invoke({"input": user_query})
    return response



def main():
    """Example usage (for testing purposes)."""
    available_models = [
        "gpt-4o", "gpt-4o-mini", "gpt3-mini", "gemini-flash-2.0",
        "claude-3.5-haiku", "llama-3.3-70b"
    ]
    print("Available models:", ", ".join(available_models))
    model_name = input("Enter the model name: ")
    user_query = input("Enter your query: ")

    response = generate_response(model_name, user_query)
    print(f"Response from {model_name}: {response}")


if __name__ == "__main__":
    main()