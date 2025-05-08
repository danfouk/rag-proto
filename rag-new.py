from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://elasticsearch-es-http.default.svc:9200/",
    api_key="gqcx0Kb5T-io3bgL1R3tiA"
)
# API key should have cluster monitor rights
print(client.info())
