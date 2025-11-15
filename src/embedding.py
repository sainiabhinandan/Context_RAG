from typing import List, Any 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np
from sentence_transformers import SentenceTransformer
from data_loader import load_all_documents






class EmbeddingPipeline:
    def __init__(self,Embedding_model: str= "all-MiniLM-L6-v2", chunk_size: int= 1000, chunk_overlap: int = 200):
       self.chunk_size = chunk_size
       self.chunk_overlap=chunk_overlap
       self.Embedding_model=SentenceTransformer(Embedding_model)
       print(f"using {Embedding_model} for embedding")


    def doc_chunker(self,documents: List[Any])-> List[Any]:
        splitter= RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks= splitter.split_documents(documents)
        print(f"chunking {len(documents)} documents in {len(chunks)} chunks ")
        return chunks
    
    
    def chunk_embedder(self,chunks: List[Any])-> np.ndarray:
        
        texts=[]
        for chunk in chunks:
            text=chunk.page_content
            texts.append(text)

        #texts= [chunk.page_content for chunk in chunks]  #is another way to write it.
        print(f"[INFO] Generating embeddings for {len(texts)} chunks...")
        embeddings = self.Embedding_model.encode(texts, show_progress_bar=True)
        print(f"[INFO] Embeddings shape: {embeddings.shape}")
        return embeddings 
    


        


        










# Example usage
# if __name__ == "__main__":

#     docs= load_all_documents("..\\data")
#     embedder=EmbeddingPipeline(chunk_size = 1000, chunk_overlap = 200)
#     chunks =embedder.doc_chunker(docs)
#     embeddings= embedder.chunk_embedder(chunks)
#     print("example embedding ", embeddings[1] if len(embeddings)>0 else None)
    
