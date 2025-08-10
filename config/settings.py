import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/faiss_index")
TASKS_DB_PATH = os.getenv("TASKS_DB_PATH", "./data/tasks.db")
