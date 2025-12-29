from .embeddings import embed
from .vector_store import collection,client
import uuid

def train(text):
  vec = embed(text)
  collection.add(ids=[str(uuid.uuid4())],documents=[text], embeddings=[vec])
   