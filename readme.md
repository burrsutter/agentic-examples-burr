Each directory has its own standalone example per framework

The test is to answer the following question:

```
How many seconds would it take for a leopard at full speed to run through Pont des Arts?
```

This prompt came from the smolagents getting started example, therefore perhaps an unfair test for the other frameworks.  Depending on the framework, the agent attempts to scrape the web for "length of pont des arts" and "top speed of leopard" then perform a converstion and calculation, perhaps via code generation or interactions with the LLM.

note: the answer should be about 9.6 seconds and it seems not every execution succeeds.


| Model+Server                 | smolagents | phidata | langgraph | llamaindex | bee   | crewai | autogen | atomic  |
| ---------------------------- | ---------- | ------- | --------- | ---------- | ----- | ------ | ------- | ------- |
| gpt4o at openai.com          | 9.62       | 9.62    | 9.62      | 9.6        | 9.6   |        |         |         |
| qwen2.5-coder:32b            | 9.62       | fail    | fail      | fail       |       |        |         |         |
| deepseek-r1-distill-qwen-14b | fail       | 4.04    | ?         | ?          |       |        |         |         |
| granite-3-8b-instruct        | fail       | fail    | 9.6       | fail       |       |        |         | 9.96    |

As of Feb 3 a web page has the answer and it could be that some of our frameworks are reacting to that finding

https://blog.csdn.net/weixin_36829761/article/details/144985939

An alternative is the following query

```
How many seconds would it take for a leopard tortoise at full speed to run through Pont des Arts?
```

### OpenAI 

OpenAI https://platform.openai.com/api-keys

```
export MODEL_NAME="gpt-4o"
export INFERENCE_SERVER_URL="https://api.openai.com/v1"
export API_KEY= go get it
```

### MaaS 

https://maas.apps.prod.rhoai.rh-aiservices-bu.com/

#### granite-3-8b-instruct

##### Litellm
```
export MODEL_NAME="openai/granite-3-8b-instruct"
export INFERENCE_SERVER_URL="https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1"
export API_KEY= go get it
```

##### not-Litellm
```
export MODEL_NAME="granite-3-8b-instruct"
export INFERENCE_SERVER_URL="https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1"
export API_KEY= go get it
```


#### deepseek-r1-distill-qwen-14b

##### Litellm
```
export MODEL_NAME="openai/deepseek-r1-distill-qwen-14b"
export INFERENCE_SERVER_URL="https://deepseek-r1-distill-qwen-14b-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1"
export API_KEY= go get it
```

##### not-Litellm
```
export MODEL_NAME="deepseek-r1-distill-qwen-14b"
export INFERENCE_SERVER_URL="https://deepseek-r1-distill-qwen-14b-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1"
export API_KEY= go get it
```


### Ollama

#### qwen2.5-coder:14b-instruct-fp16

```
export MODEL_NAME="ollama/qwen2.5-coder:14b-instruct-fp16"
export INFERENCE_SERVER_URL="http://localhost:11434"
export API_KEY=nothing
```

#### llama3.2:3b-instruct-fp16

```
export MODEL_NAME="ollama/llama3.2:3b-instruct-fp16"
export INFERENCE_SERVER_URL="http://localhost:11434"
export API_KEY=nothing
```


### remote ilab server

uses a port forwarding trick

```
export MODEL_NAME="openai//var/home/instruct/.cache/instructlab/models/Qwen/Qwen2.5-Coder-32B-Instruct"
export INFERENCE_SERVER_URL="http://localhost:8000/v1"
export API_KEY=nothing
# or
export MODEL_NAME="openai//var/home/instruct/.cache/instructlab/models/mistralai/Mistral-Small-24B-Instruct-2501"
INFERENCE_SERVER_URL="http://localhost:8000/v1"
API_KEY = "none"
```

```
curl $INFERENCE_SERVER_URL/models \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json"
```

