
from data_loader import load_all_documents
from vectorstore import FaissVectorStore
from search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    #print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    x= True
    while x:
        q= input("Enter your query (or 'exit' to quit): ")
        if q.lower() == 'exit':
            break
        query = q
        summary = rag_search.search_and_summarize(query, top_k=5)
        print("Summary:", summary)
        
   
