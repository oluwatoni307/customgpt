from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
pine_key = os.getenv('pine_key')
api_key = os.getenv('api_key')



embeddings = OpenAIEmbeddings(api_key=api_key, model="text-embedding-3-small")


  # Initialize Pinecone with new method
pc = Pinecone(api_key=pine_key)

        # Create or get index
index_name = "docs"


        # Get the index
index = pc.Index(index_name)

        # Initialize PineconeVectorStore
vector_store = PineconeVectorStore(
            index=index,
            embedding=embeddings,
        )