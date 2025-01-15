from data import data as document_content

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import ChatMessage, FunctionMessage
from langchain_core.documents import Document


def extract_short_messages(content: str, max_length=350):
    """
    Extracts messages shorter than a defined length.

    Args:
        content (str): The entire document content as a string.
        max_length (int): Maximum length of a message to be considered "short."

    Returns:
        list: A list of full message blocks shorter than the defined length.
    """
    # Split the content by dividers (`_____`)
    sections = content.split("_____")

    short_messages = []
    for section in sections:
        if section.strip():  # Skip empty sections
            # Extract the message text
            if "Text: " in section:
                message_text = section.split("Text: ")[-1].strip()
            else:
                message_text = section.strip()
            # Check if the message is shorter than the defined length
            if len(message_text) <= max_length:
                short_messages.append(section.strip())

    return short_messages


def extract_long_messages(content: str, min_length=500):
    """
    Extracts messages longer than a defined length.

    Args:
        content (str): The entire document content as a string.
        min_length (int): Minimum length of a message to be considered "long."

    Returns:
        list: A list of full message blocks longer than the defined length.
    """
    # Split the content by dividers (`_____`)
    sections = content.split("_____")

    long_messages = []
    for section in sections:
        if section.strip():  # Skip empty sections
            # Extract the message text
            if "Text: " in section:
                message_text = section.split("Text: ")[-1].strip()
            else:
                message_text = section.strip()
            # Check if the message is longer than the defined length
            if len(message_text) > min_length:
                long_messages.append(section.strip())

    return long_messages


def write_to_file(content, filename="output.txt"):
    """
    Write content to a file in the current directory
    Args:
        content: Content to write
        filename: Target filename (default: output.txt)
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(content))
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


# Extract short messages (shorter than 50 characters)
short_messages = extract_short_messages(document_content, max_length=500)
success = write_to_file(short_messages, "short_messages.txt")


from util import vector_store


def push_to_store(insights):
    docs = [Document(page_content=str(insight)) for insight in insights]
    vector_store.add_documents(documents=docs)
    return


# # Extract long messages (longer than 50 characters)
# long_messages = extract_long_messages(document_content, min_length=350)
# print("Long Messages:")
# for message in long_messages:
#     print(message)
#     print("-----")


from langchain_openai import ChatOpenAI

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('api_key')


llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

embeddings = OpenAIEmbeddings(api_key=api_key, model="text-embedding-3-small")


from Models import *


def return_semantic_chunk(message_list: list[dict]):
    # returns semantic chunks and the updated chunk
    semantic_chunk = message_list[:45]
    updated_chunk = message_list[38:]
    return semantic_chunk, updated_chunk


def process_chunk(input):
    # return a dict of metadata and content
    system = """You will receive a single message or a list of messages. Your task is to extract:

Key points: The most important and relevant pieces of information.
Actions: Only meaningful tasks or instructions that hold context or are actionable. Skip vague or redundant instructions.
Conclusions: Final decisions, outcomes, or significant takeaways. Only include conclusions that provide meaningful insights.
If a section has no meaningful information, leave it out.
    """

    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{user_input}")])
    agent = prompt | llm | StrOutputParser()
    response= agent.invoke({"user_input": (input)})
   
    return response


def process():
    messages = extract_long_messages(document_content)
    docs = []
    for chunk in messages:
        # chunk, short_messages = return_semantic_chunk(short_messages)
        insight = process_chunk(chunk)
        
        docs.append(insight)
    push_to_store(docs)
    return

if __name__ == "__main__":
    process()
