import ollama
from prompt import SYSTEM_PROMPT
from embeddings import embed_texts
from confidence import compute_confidence

def needs_retrieval(question):
    return True

def run_agent(question, retriever):
    if needs_retrieval(question):
        context = retriever(question)
    else:
        context = []

    if not context:
        return "Insufficient information in provided documents."

    context_text = "\n\n".join(
    f"[{c['meta']['source']} | chunk {c['meta']['chunk_id']}]: {c['text']}"
    for c in context
)

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context_text}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    confidence = compute_confidence(answer, context, embed_texts)

    return f"{answer}\n\nConfidence score: {confidence:.2f}"

    


