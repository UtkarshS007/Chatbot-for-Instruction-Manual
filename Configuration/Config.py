import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional, but recommended)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Access your API key from .env variable
VECTOR_STORE_PATH = "data/embeddings/"  # Path to store vector embeddings