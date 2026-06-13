import streamlit as st
import tempfile
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="PDF QA",
    page_icon="📄"
)

st.title("📄 PDF Question Answering")

# Lazy imports
@st.cache_resource
def get_embeddings():
    from langchain_huggingface import HuggingFaceEmbeddings

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

if "db" not in st.session_state:
    st.session_state.db = None

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Process PDF"):

        with st.spinner("Processing PDF..."):

            from langchain_community.document_loaders import PyPDFLoader
            from langchain_text_splitters import RecursiveCharacterTextSplitter
            from langchain_community.vectorstores import FAISS

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_file:

                temp_file.write(uploaded_file.read())
                pdf_path = temp_file.name

            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )

            chunks = splitter.split_documents(documents)

            embeddings = get_embeddings()

            db = FAISS.from_documents(
                chunks,
                embeddings
            )

            st.session_state.db = db

        st.success("PDF processed successfully!")

question = st.text_input(
    "Ask a question:"
)

if st.button("Get Answer"):

    if st.session_state.db is None:
        st.warning(
            "Please upload and process a PDF first."
        )

    elif not question.strip():
        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner("Searching..."):

            results = st.session_state.db.similarity_search(
                question,
                k=3
            )

        st.subheader("Top Matches")

        for idx, doc in enumerate(results, start=1):

            st.markdown(f"### Match {idx}")
            st.write(doc.page_content)