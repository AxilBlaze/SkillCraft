import os

def ensure_vector_store_exists():
    """Ensure the vector store directory exists."""
    vector_store_path = os.path.join(os.path.dirname(__file__), '../../vector_store')
    os.makedirs(vector_store_path, exist_ok=True)
    return vector_store_path 