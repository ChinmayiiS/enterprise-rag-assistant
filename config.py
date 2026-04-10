import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5
VECTOR_PATH = "vectorstore/faiss_index"
