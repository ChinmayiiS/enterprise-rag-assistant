# Enterprise RAG Assistant

## Overview
Production-ready Retrieval-Augmented Generation (RAG) system
for querying enterprise documents.

## Features
- Multi-hop retrieval (FAISS)
- Prompt engineering
- FastAPI deployment
- Evaluation framework

## Architecture
User Query → Retriever → LLM → Response

## Setup
export OPENAI_API_KEY=your_key

pip install -r requirements.txt

## Run
python app/ingestion.py   # create embeddings

uvicorn app.main:app --reload

## API
POST /ask
{
  "query": "your question"
}
