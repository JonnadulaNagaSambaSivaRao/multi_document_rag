<div align="center">

# 📚🤖 Multi-Document RAG System

### 🚀 Retrieval-Augmented Generation (RAG) using **Python**, **LangChain**, **Groq**, **ChromaDB**, and **HuggingFace Embeddings**

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-Vector_DB-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=for-the-badge"/>

### 🔍 Ask Questions Across Multiple Documents & Web Pages

</div>

---

# ✨ Features

✅ Supports multiple document formats

- 📄 PDF
- 📝 Markdown (.md)
- 📃 TXT
- 📘 DOCX
- 🌐 Web Pages

✅ Automatically splits documents into chunks

✅ Creates vector embeddings using HuggingFace

✅ Stores vectors in ChromaDB

✅ Retrieves the most relevant context

✅ Generates answers using Groq Llama 3.3 70B

✅ Displays source document

✅ Displays page number (for PDFs)

✅ Interactive terminal chat

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 🔗 LangChain | RAG Framework |
| 🤖 Groq API | Large Language Model |
| 🧠 HuggingFace | Embedding Model |
| 💾 ChromaDB | Vector Database |
| 📚 PyPDF | PDF Loader |
| 📄 Docx2txt | DOCX Loader |
| 🌐 WebBaseLoader | Website Loader |

---

# 📂 Project Structure

```text
multi_document_rag/
│
├── data/
│   ├── sample.pdf
│   ├── guide.md
│   ├── notes.txt
│   └── resume.docx
│
├── main.py
├── loader.py
├── splitter.py
├── embeddings.py
├── vector_store.py
├── rag_chain.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/multi_document_rag.git

cd multi_document_rag
```

---

## 2️⃣ Create Virtual Environment

```bash
uv venv --python 3.12
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add Environment Variable

Create a **.env**

```text
GROQ_API_KEY=your_groq_api_key
```

---

# 📥 Supported Documents

Simply place files inside the **data/** folder.

```text
data/

sample.pdf

guide.md

notes.txt

resume.docx
```

You can also provide web URLs inside your code.

Example

```python
urls = [
    "https://python.langchain.com/docs/introduction/"
]
```

---

# ▶️ Run the Project

```bash
python main.py
```

# ❓ Sample Questions

```text
What is API?

What is LangChain?

Explain Retrieval-Augmented Generation.

What skills are mentioned in the resume?

Summarize guide.md

What is Python?

What is ChromaDB?

What information is available in notes.txt?
```

---

# 🔄 Workflow

```text
                 User Question
                       │
                       ▼
          Load Local Documents + URLs
                       │
                       ▼
          Split into Smaller Chunks
                       │
                       ▼
       Generate HuggingFace Embeddings
                       │
                       ▼
            Store in ChromaDB
                       │
                       ▼
        Retrieve Relevant Chunks
                       │
                       ▼
          Send Context to Groq LLM
                       │
                       ▼
          Generate Final Answer
                       │
                       ▼
     Display Sources + Page Number
```

---

# 📦 Libraries Used

```text
langchain

langchain-community

langchain-groq

langchain-chroma

chromadb

sentence-transformers

huggingface-hub

python-dotenv

docx2txt

pypdf

beautifulsoup4

requests
```

---

# 🌟 Highlights

- 📄 Reads multiple document formats
- 🌐 Reads online documentation
- 🧠 Uses semantic search
- ⚡ Fast retrieval using ChromaDB
- 🤖 Llama-3.3-70B via Groq
- 📚 Returns answer with source file
- 📄 Displays PDF page numbers
- 💬 Interactive command-line chatbot
- 🔍 Easy to extend with more document types

---

# 🚀 Future Improvements

- 🎨 Streamlit Web Interface
- 💾 Persistent Chroma Database
- 📑 OCR Support for Scanned PDFs
- 🖼 Image Extraction
- 📊 Multiple Embedding Models
- 🔐 User Authentication
- 📂 Folder Monitoring
- 📈 Search History
- 🌍 Multi-language Support
- 📱 REST API using FastAPI

---

# 👨‍💻 Author

**Jonnadula Naga Samba Siva Rao**

🎓 Computer Science Engineering Graduate

💻 Passionate about AI, Python, LangChain, FastAPI, and Retrieval-Augmented Generation (RAG)

---

<div align="center">

## ⭐ If you found this project helpful, please give it a Star!

### Happy Coding! 🚀

<img src="https://img.shields.io/github/stars/yourusername/multi_document_rag?style=social"/>

<img src="https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python"/>

<img src="https://img.shields.io/badge/Open%20Source-Love-red?style=for-the-badge"/>

</div>
