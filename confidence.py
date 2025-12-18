from sklearn.metrics.pairwise import cosine_similarity

def compute_confidence(answer, retrieved_chunks, embed):
    context = " ".join(c["text"] for c in retrieved_chunks)
    ans_emb = embed([answer])
    ctx_emb = embed([context])
    return float(cosine_similarity(ans_emb, ctx_emb)[0][0])
