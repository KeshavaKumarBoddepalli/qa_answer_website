from indexer import DocumentIndexer
from llm import ask_llm

def answer_query(query, indexer):
    results = indexer.search(query)

    # Ensure results is a list
    if not isinstance(results, list):
        return "Error: No valid results found."

    # If no results are found, return a meaningful response
    if len(results) == 0:
        return "No relevant information found in the documentation."

    context = " ".join(results)
    return ask_llm(f"Use the following information to answer: {context}. Question: {query}")
