
Node Version Manager, install & select a v22
https://github.com/nvm-sh/nvm

```
nvm install v22.12.0
nvm use v22.12.0
```

```
node -v
v22.12.0
```

```
nvm install-latest-npm
```

```
npm -v
11.1.0
```

```
npm install
```

## OpenAI

```
export INFERENCE_SERVER_URL=https://api.openai.com/v1
export API_KEY=sk-proj-blah
export MODEL_NAME=gpt-4o
```

```
node leopard-pont-des-arts.mjs
```

## MaaS granite-3-8b-instruct

```
export INFERENCE_SERVER_URL=https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1
export API_KEY=169fc1c29353f7c41779f00834287eda
# export MODEL_NAME=granite-3-8b-instruct
```
Note: works better if the model name is NOT defined

To prove connectivity

```
curl $INFERENCE_SERVER_URL/models \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json"
```

## MaaS deepseek-r1-distill-qwen-14b

```
export INFERENCE_SERVER_URL=https://deepseek-r1-distill-qwen-14b-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1
export API_KEY=blah
# export MODEL_NAME=deepseek-r1-distill-qwen-14b
```

### Qwen2.5-Coder-32B-Instruct

```
export INFERENCE_SERVER_URL=localhost:8000/v1
export API_KEY=not-required
```
