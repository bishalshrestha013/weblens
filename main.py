from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from constants import ALLOWED_ORIGINS
from utils.ragPipeline import ingestDocument, answerQuestion

load_dotenv()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=ALLOWED_ORIGINS,
  allow_methods=["*"],
  allow_headers=["*"],
)


class IngestRequest(BaseModel):
  url: str


@app.post("/ingest")
async def ingest(request: IngestRequest):
  try:
    chunkCount = ingestDocument(request.url)
  except Exception as error:
    raise HTTPException(status_code=500, detail=str(error))

  return {"url": request.url, "chunks": chunkCount}


@app.get("/query")
async def query(q: str):
  try:
    answer = answerQuestion(q)
  except FileNotFoundError as error:
    raise HTTPException(status_code=400, detail=str(error))
  except Exception as error:
    raise HTTPException(status_code=500, detail=str(error))

  return {"query": q, "answer": answer}
