from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


_embeddings = None


def get_embeddings():
    """
    Load the HuggingFace embedding model.
    The model is loaded only once and reused.
    """

    global _embeddings

    if _embeddings is None:

        print("=" * 60)
        print("Loading Embedding Model...")
        print("=" * 60)

        _embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            },
        )

        print("Embedding Model Loaded Successfully!\n")

    return _embeddings