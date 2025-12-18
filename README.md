# # Agentic Legal & Policy QA System

## Problem Statement

Large language models can generate fluent legal answers but often hallucinate or rely on undocumented knowledge.  
In regulated domains such as law, privacy, and compliance, answers must be grounded, auditable, and refuse unsupported queries.

This project implements an agentic Retrieval-Augmented Generation (RAG) system that answers legal and policy questions strictly from provided documents, with built-in safeguards against hallucinations.

## System Overview

The system follows an agentic RAG architecture:

1. Legal and policy documents are ingested, chunked, and embedded
2. A FAISS vector index retrieves relevant document chunks
3. An agent enforces mandatory retrieval and refusal logic
4. Answers are generated strictly from retrieved context
5. A faithfulness score evaluates grounding of the answer

## Key Features

- Retrieval-Augmented Generation (RAG) using FAISS
- Agent logic with mandatory retrieval and refusal handling
- Chunk-level document citations for auditability
- Automated confidence / faithfulness scoring
- Supports multiple legal and policy documents
- CLI and Streamlit UI interfaces using shared core logic

## Documents Used

- GDPR (Regulation EU 2016/679)
- Google Privacy Policy (Effective July 2025)

The system answers questions strictly from these documents and refuses out-of-scope queries.




