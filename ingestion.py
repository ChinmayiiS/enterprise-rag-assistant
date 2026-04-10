from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from app.config import CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_PATH


def load_documents(path="data/"):
    loader = DirectoryLoader(path, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(VECTOR_PATH)
    return vector_db


if __name__ == "__main__":
    docs = load_documents()
    chunks = split_documents(docs)
    create_vectorstore(chunks)
