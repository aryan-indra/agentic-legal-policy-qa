import streamlit as st

from ingest import ingest_documents
from embeddings import embed_texts, embed_query
from vectorstore import build_index, search
from tools import retrieve_tool
from agent import run_agent


# =====================================================
# Streamlit Page Config
# =====================================================
st.set_page_config(
    page_title="Legal / Policy QA Agent",
    layout="wide"
)

st.title("📜 Legal / Policy QA Agent")
st.caption("Agentic RAG system with grounded answers and confidence scoring")

# =====================================================
# Load & Index Documents (cached)
# =====================================================
@st.cache_resource
def load_system():
    chunks, metadata = ingest_documents()
    embeddings = embed_texts(chunks)
    index = build_index(embeddings)
    return chunks, metadata, index


chunks, metadata, index = load_system()


# =====================================================
# Retriever Wrapper (same as CLI)
# =====================================================
def retriever(query):
    return retrieve_tool(
        query=query,
        index=index,
        chunks=chunks,
        metadata=metadata,
        embed_query=embed_query,
        search=search
    )


# =====================================================
# UI Input
# =====================================================
question = st.text_input(
    "Ask a legal or policy question",
    placeholder="e.g. What is considered personal data under GDPR?"
)

run = st.button("Ask")


# =====================================================
# Run Agent
# =====================================================
if run and question:
    with st.spinner("Thinking..."):
        answer = run_agent(question, retriever)

    st.subheader("Answer")
    st.write(answer)
