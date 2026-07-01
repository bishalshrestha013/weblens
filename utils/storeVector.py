from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def generateAndStoreEmbedding(chunks):
  """returns a FAISS vector store containing the embeddings of the provided chunks."""
  embedding = OpenAIEmbeddings(model="text-embedding-3-small")

  vectorStore = FAISS.from_documents(chunks, embedding)

  return vectorStore