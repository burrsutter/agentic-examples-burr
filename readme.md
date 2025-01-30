Each directory has its own standalone example per framework



### Ollama

If using ollama, test connectivity

```
ollama serve
```

```
ollama ls
```

```
NAME                                 ID              SIZE      MODIFIED
qwen2.5-coder:32b                    4bd6cbf2d094    19 GB     4 hours ago
deepseek-r1:32b                      38056bbcbb2d    19 GB     24 hours ago
deepseek-r1:14b                      ea35dfe18182    9.0 GB    2 days ago
granite3-dense:8b-instruct-q4_K_M    199456d876ee    4.9 GB    5 weeks ago
qwen2.5:7b-instruct-q4_K_M           845dbda0ea48    4.7 GB    5 weeks ago
llama3.2:3b-instruct-q4_K_M          a80c4f17acd5    2.0 GB    5 weeks ago
mistral:7b-instruct-q4_K_M           1a85656b534f    4.4 GB    5 weeks ago
phi3.5:3.8b-mini-instruct-q4_K_M     570961596984    2.4 GB    5 weeks ago
gemma2:2b-instruct-q4_K_M            cb2d06dce813    1.7 GB    5 weeks ago
nomic-embed-text:v1.5                0a109f422b47    274 MB    5 weeks ago
llama3.1:latest                      46e0c10c039e    4.9 GB    6 weeks ago
llama3.2:3b-instruct-fp16            195a8c01d91e    6.4 GB    6 weeks ago
llama3.2:1b-instruct-q4_K_M          22bc6b92eb01    807 MB    7 weeks ago
qwq:32b-preview-q4_K_M               1211a3265dc8    19 GB     2 months ago
qwen2.5:0.5b-instruct-q4_K_M         a8b0c5157701    397 MB    2 months ago
granite3-moe:3b-instruct-q4_K_M      5d8ebcfcdb80    2.1 GB    2 months ago
llama3.2-vision:11b                  38107a0cd119    7.9 GB    2 months ago
```


```
curl -X POST http://localhost:11434/api/generate -d '{"model":"mistral:7b-instruct-q4_K_M","prompt":"why is the sky blue in 10 words or less?"}'
```


### MaaS 

https://maas.apps.prod.rhoai.rh-aiservices-bu.com/

```
curl -X POST https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1/api/generate -d '{"model":"mistral:7b-instruct-q4_K_M","prompt":"why is the sky blue in 10 words or less?"}'
```