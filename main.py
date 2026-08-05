from loaders import load_documents
from splitter import split_documents
from vectordb import create_vector_db
from llm import get_llm
from rag import build_chain

def main():

    print("=" * 60)
    print("📚 Multi-Document RAG System")
    print("=" * 60)

    # Load documents
    documents = load_documents()

    # Split into chunks
    chunks = split_documents(documents)

    # Create Chroma vector database
    db = create_vector_db(chunks)

    # Load LLM
    llm = get_llm()

    # Build RAG pipeline
    rag = build_chain(llm, db)

    print("\n✅ System Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask Question: ").strip()

        if question.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        if not question:
            continue

        try:

            result = rag(question)

            print("\n" + "=" * 60)
            print("Answer")
            print("=" * 60)
            print(result["answer"])

            print("\nRetrieved Metadata")
            print("=" * 60)

            for doc in result["documents"]:
              print(doc.metadata)

            print("\nSources")
            print("=" * 60)

            seen = set()

            for doc in result["documents"]:

                source = doc.metadata.get("source", "Unknown")

                page = doc.metadata.get("page")

                if page is not None:
                         page += 1   # Convert from 0-based to 1-based page numbering
                else:
                          page = "N/A"

                key = (source, page)

                if key in seen:
                    continue

                seen.add(key)

                print(f"File : {source}")
                print(f"Page : {page}")
                print("-" * 40)

        except Exception as e:

            print("\n❌ Error")
            print(e)


if __name__ == "__main__":
    main()