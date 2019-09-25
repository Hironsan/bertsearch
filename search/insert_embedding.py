import json
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def load_dataset(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), '../data/dataset.jsonl')
    docs = load_dataset(path)

    client = Elasticsearch()
    INDEX_NAME = 'jobsearch'
    client.indices.delete(index=INDEX_NAME, ignore=[404])
    with open('index.json') as index_file:
        source = index_file.read().strip()
        client.indices.create(index=INDEX_NAME, body=source)

    bulk(client, docs)
