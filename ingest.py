from pypdf import PdfReader
from pathlib import Path

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size - overlap
    return chunks

def ingest_documents(folder="data/policies"):
    all_chunks = []
    metadata = []

    for file in Path(folder).glob("*"):
        if file.suffix == ".pdf":
            reader = PdfReader(file)
            text = "\n".join(page.extract_text() for page in reader.pages)
        else:
            text = file.read_text(encoding="utf-8")

        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata.append({
                "source": file.name,
                "chunk_id": i
            })

    return all_chunks, metadata
