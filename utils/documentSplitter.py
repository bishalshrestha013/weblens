from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitText(documents, chunkSize: int = 1000, chunkOverlap: int = 200):
  textSplitter = RecursiveCharacterTextSplitter(
    chunk_size=chunkSize,
    chunk_overlap=chunkOverlap)

  chunks = textSplitter.split_documents(documents)

  return chunks
