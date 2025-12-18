from ingest import ingest_documents
from embeddings import embed_texts, embed_query
from vectorstore import build_index, search
from tools import retrieve_tool
from agent import run_agent

chunks, metadata = ingest_documents()
embeddings = embed_texts(chunks)
index = build_index(embeddings)

def retriever(question):
    return retrieve_tool(
        question,
        index,
        chunks,
        metadata,
        embed_query,
        search
    )

while True:
    q = input("\nAsk legal question (or exit): ")
    if q.lower() == "exit":
        break
    print(run_agent(q, retriever))
