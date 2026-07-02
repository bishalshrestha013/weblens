from langchain_openai import ChatOpenAI

from constants import CHAT_MODEL, CHAT_TEMPERATURE
from utils.documentLoader import load_document
from utils.documentSplitter import splitText
from utils.storeVector import generateAndStoreEmbedding, loadVectorStore
from utils.retrieveContext import retrieveContext
from utils.generatePrompt import generatePrompt


def ingestDocument(url: str) -> int:
  """scrapes a url, splits and embeds it, persists the index, and returns the chunk count."""
  loadedDocument = load_document(url)
  chunks = splitText(loadedDocument)
  generateAndStoreEmbedding(chunks)

  return len(chunks)


def answerQuestion(query: str) -> str:
  """answers a query against the previously ingested (persisted) index."""
  vectorStore = loadVectorStore()
  context = retrieveContext(query, vectorStore)
  generatedPrompt = generatePrompt(context, query)

  llm = ChatOpenAI(model=CHAT_MODEL, temperature=CHAT_TEMPERATURE)
  answer = llm.invoke(generatedPrompt)

  return answer.content
