# ml-middleware

Middleware for HanLP, FastText and TensorFlow Serving accessing. Connect and communicate through gRPC.

## Build and Deploy

Build image from Dockerfile

```shell
docker build ml-middleware:{tag} .
```

Build container. The first two volumes are [HanLP](https://hanlp.hankcs.com/docs/install.html#server-without-internet) models and libs.
The third volume is the directory for [fastText model]().
Environment value `MOD_TAGGING_TF_RPC_SERVER` refers to TensorFlow Serving's address, which hosts prediction model.

```shell
docker run -d -p 50051:50051\
  --mount type=bind,source=/Users/lifan/jiatu/st-project/volumes/hanlp,target=/root/.hanlp\
  --mount type=bind,source=/Users/lifan/jiatu/st-project/volumes/huggingface,target=/root/.cache/huggingface\
  --mount type=bind,source=/Users/lifan/jiatu/st-project/volumes/fasttext,target=/root/models/fasttext\
  --network ml-network\
  -e MOD_TAGGING_TF_RPC_SERVER=tf-serving-cir-classify:8500\
  --name ml-middleware-0713\
  -t ml-middleware:071303
```