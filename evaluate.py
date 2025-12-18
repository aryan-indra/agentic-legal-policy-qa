from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def faithfulness(answer, context, embed):
    ans_emb = embed([answer])
    ctx_emb = embed([context])
    return cosine_similarity(ans_emb, ctx_emb)[0][0]

def evaluate_sample(answer, retrieved_chunks, embed):
    context = " ".join(c["text"] for c in retrieved_chunks)
    score = faithfulness(answer, context, embed)
    return {
        "faithfulness_score": float(score),
        "pass": score > 0.7
    }
