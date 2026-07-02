from fastapi import FastAPI
from dotenv import load_dotenv
from utils.documentLoader import load_document
from utils.documentSplitter import splitText
from utils.retrieveContext import retrieveContext
from utils.storeVector import generateAndStoreEmbedding
from utils.generatePrompt import generatePrompt
from langchain_openai import ChatOpenAI

load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root():
  loadedDocument = load_document("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")

  chunks = splitText(loadedDocument)
  vectorStore = generateAndStoreEmbedding(chunks)

  query = "What is Cristiano Ronaldo known for?"

  context = retrieveContext(query, vectorStore)

  generated_prompt = generatePrompt(context, query)

  llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
  answer = llm.invoke(generated_prompt)

  return {"answer": answer.content}
