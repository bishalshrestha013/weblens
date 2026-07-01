from langchain_community.document_loaders import WebBaseLoader

def load_document(url: str):
  loader = WebBaseLoader(url)
  scrape_data = loader.load()

  return scrape_data
