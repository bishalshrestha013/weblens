from langchain_core.prompts import PromptTemplate

def generatePrompt(context, query):
    """returns a prompt based on the context and query"""
    template="""
      You are a helpful assistant. Answer only from the provided context. If the context is insufficient, just say 'I don't know'.\
      Context: {context}
      Query: {query}"""
    
    prompt = PromptTemplate(
        input_variables=["context", "query"],
        template=template,
    )

    return prompt.invoke({"context": context, "query": query})
