from flask import Flask, render_template, jsonify, request, redirect, url_for
from elasticsearch import Elasticsearch
from bert_serving.client import BertClient
bc = BertClient(output_fmt='list')
client = Elasticsearch()
SEARCH_SIZE = 10
INDEX_NAME = "jobsearch"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search')
def analyzer():
    query = request.args.get('q')
    query_vector = bc.encode([query])[0]

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, doc['text_vector']) + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }

    response = client.search(
        index=INDEX_NAME,
        body={
            "size": SEARCH_SIZE,
            "query": script_query,
            "_source": {"includes": ["title", "text"]}
        }
    )
    from pprint import pprint
    pprint(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run()
