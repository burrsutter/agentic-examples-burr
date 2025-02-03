## OpenAI
Requires vllm or openai api-key

https://platform.openai.com/api-keys

Requires tavily api-key

https://app.tavily.com/

```
python3.11 -m venv .venv
source .venv/bin/activate
cp .env.example .env
```

Edit .env, providing the api-keys

```
pip install --upgrade pip
pip install -r requirements.txt
```

```
python leopard-pont-des-arts.py
```
