import chromadb
from chromadb.config import Settings

client = chromadb.Client(
   Settings(
        persist_directory="./chroma_db",
        anonymized_telemetry=False
    )
)
collection = client.get_or_create_collection("knowledge")