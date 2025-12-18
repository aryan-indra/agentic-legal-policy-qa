def retrieve_tool(query, index, chunks, metadata, embed_query, search):
    query_emb = embed_query(query)
    idxs, _ = search(index, query_emb, top_k=5)

    results = []
    for i in idxs:
        results.append({
            "text": chunks[i],
            "meta": metadata[i]
        })
    return results
