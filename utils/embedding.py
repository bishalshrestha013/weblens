from langchain_openai import OpenAIEmbeddings

from constants import EMBEDDING_MODEL


def getEmbedding():
  """returns the shared embedding model used for both ingestion and querying."""

  return OpenAIEmbeddings(model=EMBEDDING_MODEL)
