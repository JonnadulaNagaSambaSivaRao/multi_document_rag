import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ==============================
# Groq Configuration
# ==============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Groq Model
MODEL_NAME = "llama-3.3-70b-versatile"

# ==============================
# Chroma Configuration
# ==============================

CHROMA_DB_DIR = "chroma_db"

# ==============================
# Data Folder
# ==============================

DATA_FOLDER = "data"

# ==============================
# Website URLs
# ==============================

WEB_URLS = [
    "https://python.langchain.com/docs/introduction/"
]

# ==============================
# Text Splitter Configuration
# ==============================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# ==============================
# Embedding Model
# ==============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==============================
# Retriever Configuration
# ==============================

TOP_K = 3