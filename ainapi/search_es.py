from elasticsearch import Elasticsearch
from config import ES_CLIENT_URL

# es_client = Elasticsearch(["elastic:changeme@localhost:9200"])
es_client = Elasticsearch([ES_CLIENT_URL])

def get_es_results(q):
    query_body = {
        "_source": ["nome*", "area*", "campus", "centro", "departamento", "email", "email2", "foto", "idcnpq",
                    "informacoes_mostradas_nosite", "nome", "publico", "sigla_*", "tipo_*", "uid"],
        "query": {
            "multi_match": {
                'query': q,
                'fields': ["lattes2", "lattes", "area*", "nome", "departamento", "campus", "sigla_*"]
            },
        }
    }
    result = es_client.search(index="lattesuser", body=query_body, size=10000)
    return [ item['_source'] for item in result['hits']['hits'] ]
