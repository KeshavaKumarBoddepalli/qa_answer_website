import faiss
import numpy as np
import os
from transformers import AutoTokenizer, AutoModel
import torch

INDEX_PATH = "faiss_index.bin"

class DocumentIndexer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        
        self.index = faiss.IndexFlatL2(384)  # Vector index
        self.docs = []  # Stores document texts

        if os.path.exists(INDEX_PATH):  # Load existing FAISS index
            self.load_index()

    def embed_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            embeddings = self.model(**inputs).last_hidden_state.mean(dim=1)
        return embeddings.numpy()

    def index_documents(self, docs):
        """Indexes the given documents and saves the index."""
        vectors = np.vstack([self.embed_text(doc) for doc in docs])
        self.index.add(vectors)
        self.docs.extend(docs)  # Store texts

        self.save_index()  # Persist the index to disk

    def save_index(self):
        """Saves the FAISS index to disk."""
        faiss.write_index(self.index, INDEX_PATH)
        with open("docs.txt", "w", encoding="utf-8") as f:
            for doc in self.docs:
                f.write(doc + "\n")

    def load_index(self):
        """Loads FAISS index from disk."""
        self.index = faiss.read_index(INDEX_PATH)
        with open("docs.txt", "r", encoding="utf-8") as f:
            self.docs = f.read().splitlines()

    def search(self, query, top_k=3):
        """Retrieves the most relevant document matches."""
        if len(self.docs) == 0:
            return ["Error: No documents indexed. Please scrape and index documentation first."]
        
        query_vector = self.embed_text(query)
        distances, indices = self.index.search(query_vector, top_k)

        return [self.docs[i] for i in indices[0] if i < len(self.docs)]
