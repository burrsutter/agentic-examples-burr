
```
python3.11 -m venv venv
source venv/bin/activate
```

```
pip install -q langchain-openai termcolor langchain_community duckduckgo_search==7.1.0 wikipedia openapi-python-client==0.12.3 langgraph langchain_experimental
```

OpenAI.com

```
export INFERENCE_SERVER_URL=https://api.openai.com/v1
export API_KEY=sk-proj-blah-blah
export MODEL_NAME="gpt-4o"
```

Or MaaS

```
export INFERENCE_SERVER_URL=https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1
export API_KEY=
export MODEL_NAME="granite-3-8b-instruct"
```

Or 4GPU Server with Qwen2.5-Coder-32B-Instruct

```
export INFERENCE_SERVER_URL=
```

```
python leopard-pont-des-arts.py
```
