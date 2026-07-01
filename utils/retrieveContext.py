from langchain_community.vectorstores import FAISS

def retrieveContext(query: str, vectorStore: FAISS):
    """returns the context of the document based on the query"""
    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    context = retriever.invoke(query)

    return context