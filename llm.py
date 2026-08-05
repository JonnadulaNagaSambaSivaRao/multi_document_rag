from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME


_llm = None


def get_llm():
    """
    Create and return a Groq LLM instance.
    The model is initialized only once.
    """

    global _llm

    if _llm is None:

        print("=" * 60)
        print("Connecting to Groq...")
        print("=" * 60)

        _llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0,
            max_tokens=1024,
        )

        print(f"Model : {MODEL_NAME}")
        print("Groq Connected Successfully!\n")

    return _llm