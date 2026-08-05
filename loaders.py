from dotenv import load_dotenv
import os

load_dotenv()
import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    WebBaseLoader,
    UnstructuredMarkdownLoader,
)

from langchain_community.document_loaders import UnstructuredMarkdownLoader

from config import DATA_FOLDER, WEB_URLS


def load_documents():
    """
    Load all supported documents from the data folder
    and from configured web URLs.
    """

    documents = []

    if not os.path.exists(DATA_FOLDER):
        raise FileNotFoundError(
            f"Data folder '{DATA_FOLDER}' does not exist."
        )

    print("\nLoading local documents...\n")

    for file_name in os.listdir(DATA_FOLDER):

        file_path = os.path.join(DATA_FOLDER, file_name)

        try:

            if file_name.lower().endswith(".pdf"):

                docs = PyPDFLoader(file_path).load()

            elif file_name.lower().endswith(".txt"):

                docs = TextLoader(
                    file_path,
                    encoding="utf-8"
                ).load()

            elif file_name.lower().endswith(".md"):

                docs = UnstructuredMarkdownLoader(
                    file_path
                ).load()

            elif file_name.lower().endswith(".docx"):

                docs = Docx2txtLoader(
                    file_path
                ).load()

            else:
                continue

            documents.extend(docs)

            print(f"✓ Loaded {file_name}")

        except Exception as e:

            print(f"✗ Failed to load {file_name}")

            print(e)

    if WEB_URLS:

        print("\nLoading web pages...\n")

        for url in WEB_URLS:

            try:

                docs = WebBaseLoader(url).load()

                documents.extend(docs)

                print(f"✓ Loaded {url}")

            except Exception as e:

                print(f"✗ Failed to load {url}")

                print(e)

    print(f"\nTotal documents loaded: {len(documents)}\n")

    return documents