from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from app.config import VECTOR_PATH, TOP_K


def load_retriever():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTOR_PATH, embeddings)
    return db.as_retriever(search_kwargs={"k": TOP_K})


def multi_hop_retrieval(query, retriever):
    docs_1 = retriever.get_relevant_documents(query)

    refined_query = query + " more context"
    docs_2 = retriever.get_relevant_documents(refined_query)

    return docs_1 + docs_2
