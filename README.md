# pdf-rag-question-answering
Question Answering System for PDFs using RAG, LangChain, HuggingFace Embeddings, and FAISS.
# 📄 PDF RAG Question Answering System

A beginner-friendly Retrieval-Augmented Generation (RAG) project that allows users to ask questions from PDF documents using semantic search.

## 🚀 Features

* Load PDF documents
* Split text into smaller chunks
* Generate embeddings using Sentence Transformers
* Store embeddings in FAISS Vector Database
* Perform semantic similarity search
* Retrieve relevant content based on user queries
* Interactive command-line interface

## 🛠️ Tech Stack

* Python
* LangChain
* HuggingFace Embeddings
* FAISS
* PyPDF
* Sentence Transformers

## 📂 Project Workflow

```text
PDF
 ↓
Document Loading
 ↓
Text Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Semantic Search
 ↓
Relevant Answer
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pdf-rag-question-answering.git
cd pdf-rag-question-answering
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Place your PDF file in the project directory and rename it to:

```text
sample.pdf
```

Run the application:

```bash
python app.py
```

Example:

```text
Question: What is a dictionary?

Answer:
Dictionary is an unordered collection of items.
Dictionary stores a (key, value) pair.
```

## 📁 Project Structure

```text
pdf-rag-question-answering/
│
├── app.py
├── sample.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Learning Outcomes

This project helped me understand:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* LangChain Fundamentals
* Document Processing Pipelines

## 🔮 Future Improvements

* Streamlit Web Interface
* Multi-PDF Support
* Chat History
* Gemini/OpenAI Integration
* Source Citation & Page References
* Persistent Vector Storage

## 🤝 Contributing

Feel free to fork the repository and submit improvements.

## 📜 License

This project is open-source and available under the MIT License.
