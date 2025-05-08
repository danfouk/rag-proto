import json
import os
from llama_index.core import Document, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from dotenv import load_dotenv


def get_documents_from_jsonl(file="./data/conversations.json"):
    """Reads a json file and returns list of Documents"""
    with open(file=file, mode='r') as f:
        conversations_dict = json.load(f.read())
    # Build Document objects using fields of interest.
    documents = [Document(text=item['conversation'],
                          metadata={"conversation_id": item['conversation_id']})
                 for
                 item in conversations_dict]
    return documents
