
import warnings
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

warnings.filterwarnings("ignore")

# -------------------------
# Load PDF
# -------------------------
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print(f"Pages Loaded: {len(documents)}")

# -------------------------
# Create Smaller Chunks
# -------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# -------------------------
# Print All Chunks
# -------------------------
print("\n===== ALL CHUNKS =====")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}")
    print("-" * 30)
    print(chunk.page_content[:200])

# -------------------------
# Embeddings
# -------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------
# FAISS
# -------------------------
db = FAISS.from_documents(chunks, embeddings)

print("\nVector Database Ready")

# -------------------------
# Ask Questions
# -------------------------
while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    results = db.similarity_search(
        question,
        k=3
    )

    print("\nTop Matches:\n")

    for i, doc in enumerate(results, start=1):

        text = doc.page_content.replace("\n", " ")
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

        print(f"\nMatch {i}")
        print("-" * 20)
        print(text)

