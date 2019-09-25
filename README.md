# BERT Search by using Elasticsearch

- [Text similarity search in Elasticsearch using vector fields \| Elastic Blog](https://www.elastic.co/jp/blog/text-similarity-search-with-vectors-in-elasticsearch)
- [jtibshirani/text\-embeddings](https://github.com/jtibshirani/text-embeddings)

## Preparation

```bash
$ wget https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/dataset.jsonl -P data/
$ wget https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip
$ unzip cased_L-12_H-768_A-12.zip
$ bert-serving-start -model_dir cased_L-12_H-768_A-12/ -num_worker=1
```

```bash
$ docker-compose up
$ python insert_embedding.py
```


## Text Similarity Search

```bash
$ cd search/server
$ python app.py
```
