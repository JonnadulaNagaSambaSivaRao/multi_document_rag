import os
import shutil

from langchain_chroma import Chroma

from embeddings import get_embeddings
from config import CHROMA_DB_DIR


def create_vector_db(chunks):
    """
    Create a new Chroma vector database.
    """

    # Remove old database if it exists
    if os.path.exists(CHROMA_DB_DIR):
        shutil.rmtree(CHROMA_DB_DIR)

    print("=" * 60)
    print("Creating Chroma Vector Database...")
    print("=" * 60)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=CHROMA_DB_DIR,
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")
    print("Vector Database Created Successfully!\n")

    return vector_db


def load_vector_db():
    """
    Load an existing Chroma vector database.
    """

    if not os.path.exists(CHROMA_DB_DIR):
        raise FileNotFoundError(
            "Chroma database not found. Run indexing first."
        )

    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=get_embeddings(),
    )