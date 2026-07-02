import os

from langchain_community.vectorstores import FAISS

from constants import FAISS_INDEX_PATH
from utils.embedding import getEmbedding


def generateAndStoreEmbedding(chunks):
  """embeds the chunks, persists a FAISS index to disk, and returns the store."""
  vectorStore = FAISS.from_documents(chunks, getEmbedding())
  vectorStore.save_local(FAISS_INDEX_PATH)

  return vectorStore


def loadVectorStore():
  """loads the persisted FAISS index from disk."""
  if not os.path.exists(FAISS_INDEX_PATH):
    raise FileNotFoundError("No document has been ingested yet. Call /ingest first.")

  return FAISS.load_local(
    FAISS_INDEX_PATH,
    getEmbedding(),
    allow_dangerous_deserialization=True,
  )
