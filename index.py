import json
import os
from llama_index.core import Document, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from dotenv import load_dotenv


def get_documents_from_jsonl(file="./data/conversations.json"):
    """Reads a JSON file and returns a list of Documents"""
    try:
        with open(file, mode='r') as f:
            conversations_dict = json.load(f)
        # Build Document objects using fields of interest.
        documents = [Document(text=item['conversation'],
                              metadata={"conversation_id": item['conversation_id']})
                     for item in conversations_dict]
        return documents
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file}.")
        return []


# Example usage
if __name__ == "__main__":
    documents = get_documents_from_jsonl()
print(documents)


# Load .env file contents into env
# ELASTIC_CLOUD_ID and ELASTIC_API_KEY are expected to be in the .env file.
load_dotenv('.env')

# ElasticsearchStore is a VectorStore that
# takes care of ES Index and Data management.
es_vector_store = ElasticsearchStore(index_name="calls",
                                     vector_field='conversation_vector',
                                     text_field='conversation',
                                     es_url=os.getenv("ES_URL"),
                                     es_user=os.getenv("ELASTIC_USER"),
                                     es_password=os.getenv("ELASTIC_PASSWORD"),
                                     es_api_key=os.getenv("ELASTIC_API_KEY"))
