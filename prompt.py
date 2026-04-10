from langchain.prompts import PromptTemplate

template = """
You are an enterprise AI assistant.

Rules:
- Answer ONLY from the context
- If not found, say "Insufficient data"
- Be concise and accurate

Context:
{context}

Question:
{question}
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)
