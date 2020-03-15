#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

# es_client = Elasticsearch(["elastic:changeme@localhost:9200"])
es_client = Elasticsearch(["200.136.215.138:9200"])

user_request = "vidro"
query_body = {
    "_source": ["nome*", "area*", "campus", "centro", "departamento", "email", "email2", "foto", "idcnpq",
                "informacoes_mostradas_nosite", "nome", "publico", "sigla_*", "tipo_*", "uid"],
    "query": {
        "multi_match": {
            'query': user_request,
            'fields': ["lattes2", "lattes", "area*", "nome", "departamento", "campus", "sigla_*"]
        },
    }
}

# call the client's search() method, and have it return results
result = es_client.search(index="lattesuser", body=query_body, size=10000)

# see how many "hits" it returned using the len() function
print("total hits:", len(result["hits"]["hits"]))
print("query hits:", result["hits"]["hits"])

all_hits = result['hits']['hits']

# iterate the nested dictionaries inside the ["hits"]["hits"] list
def seeHits(hits):
    for num, doc in enumerate(hits):
        print("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")

        # Use 'iteritems()` instead of 'items()' if using Python 2
        for key, value in doc.items():
            print(key, "-->", value)

        # print a few spaces between each doc for readability
        print("\n\n")

query_body = {
    "query": {
        "bool": {
            "must": {
                "match": {
                    "some_field": user_request
                }
            }
        }
    }
}

query_body1 = {
    "query": {
        "match": {
            "some_field": "search_for_this"
        }
    }
}

query_body2 = {
    "query": {
        "match_all": {}
    }
}

query_body3 = {
    "query": {
        "match": {
            "_all": "search body"
        }
    }
}


# from elasticsearch_dsl import MultiSearch, Search
#
# ms = MultiSearch(index='post')
#
# ms = ms.add(Search().filter('term', tags='title'))
# ms = ms.add(Search().filter('term', tags='body'))
#
# responses = ms.execute()