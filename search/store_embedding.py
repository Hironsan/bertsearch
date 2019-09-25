import json
import os
import pandas as pd
from bert_serving.client import BertClient
bc = BertClient(output_fmt='list')


def get_request(doc, emb):
    return {
        '_op_type': 'index',
        '_index': 'jobsearch',
        'text': doc['text'],
        'title': doc['title'],
        'text_vector': emb
    }


def load_dataset(path):
    docs = []
    df = pd.read_csv(path)
    df.fillna('', inplace=True)
    for row in df.iterrows():
        series = row[1]
        title = '{} {}'.format(series.Company, series.Title)
        text = '{} {} {}'.format(series.JobDescription, series.JobRequirment, series.RequiredQual)
        doc = {
            'title': title,
            'text': text
        }
        docs.append(doc)
    return docs


def bulk_predict(docs, batch_size=256):
    for i in range(0, len(docs), batch_size):
        batch_docs = docs[i: i+batch_size]
        embeddings = bc.encode([doc['text'] for doc in batch_docs])
        for doc, emb in zip(batch_docs, embeddings):
            yield get_request(doc, emb)


if __name__ == '__main__':
    # Loading job dataset.
    path = os.path.join(os.path.dirname(__file__), '../data/dataset.jsonl')
    docs = load_dataset('jobposts/data job posts.csv')
    gen = bulk_predict(docs)
    with open(path, 'w') as f:
        for dic in gen:
            f.write(json.dumps(dic) + '\n')
