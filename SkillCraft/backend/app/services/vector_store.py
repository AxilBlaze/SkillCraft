from flask import current_app
import numpy as np
import os
import pickle

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.store_path = None
        
    def initialize(self):
        """Initialize or load the vector store."""
        if self.store_path is None:
            self.store_path = current_app.config['VECTOR_STORE_PATH']
            
        if os.path.exists(self.store_path):
            try:
                with open(self.store_path, 'rb') as f:
                    self.vectors = pickle.load(f)
            except Exception as e:
                print(f"Error loading vectors: {str(e)}")
                self.vectors = []
    
    def add_vectors(self, vectors, metadata=None):
        """Add vectors to the store."""
        if self.store_path is None:
            self.initialize()
            
        vectors = np.array(vectors).astype('float32')
        self.vectors.extend(vectors)
        self.save_store()
    
    def search(self, query_vector, k=5):
        """Search for similar vectors using cosine similarity."""
        if self.store_path is None:
            self.initialize()
            
        if not self.vectors:
            return [], []
            
        query_vector = np.array(query_vector).astype('float32')
        vectors = np.array(self.vectors)
        
        # Compute cosine similarity
        similarities = np.dot(vectors, query_vector) / (
            np.linalg.norm(vectors, axis=1) * np.linalg.norm(query_vector)
        )
        
        # Get top k indices
        indices = np.argsort(similarities)[-k:][::-1]
        distances = similarities[indices]
        
        return distances, indices
    
    def save_store(self):
        """Save vectors to disk."""
        if self.store_path is not None:
            try:
                os.makedirs(os.path.dirname(self.store_path), exist_ok=True)
                with open(self.store_path, 'wb') as f:
                    pickle.dump(self.vectors, f)
            except Exception as e:
                print(f"Error saving vectors: {str(e)}")

# Create singleton instance
vector_store = VectorStore()

def get_vector_store():
    """Get the vector store instance."""
    if vector_store.store_path is None:
        vector_store.initialize()
    return vector_store 