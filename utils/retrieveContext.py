from langchain_community.vectorstores import FAISS

from constants import RETRIEVER_K

def retrieveContext(query: str, vectorStore: FAISS):
    """returns the context of the document based on the query"""
    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": RETRIEVER_K})

    retrieved_docs = retriever.invoke(query)

    return "\n\n".join(docs.page_content for docs in retrieved_docs)