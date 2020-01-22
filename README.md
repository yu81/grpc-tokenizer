# grpc-tokenizer
Sentence tokenization server in python using grpc for microservices.

# How to use

- run with python command.

`python src/app/server_grpc.py`

- or with docker.

```shell
docker build -t tokenizer .
docker run -p 6565:6565 tokenizer
```


