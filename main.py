from fastapi import FastAPI
from dotenv import load_dotenv
from utils.documentLoader import load_document
from utils.documentSplitter import splitText
from utils.storeVector import generateAndStoreEmbedding

load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root():
  loadedDocument = load_document("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")

  chunks = splitText(loadedDocument)
  vectorStore = generateAndStoreEmbedding(chunks)

  print(vectorStore.index_to_docstore_id)

  return {"Hello": "whats up"}
