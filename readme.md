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


```
How many seconds would it take for a leopard tortoise at full speed to run through Pont des Arts?
```


### MaaS 

https://maas.apps.prod.rhoai.rh-aiservices-bu.com/

```
curl $INFERENCE_SERVER_URL/models \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json"
```

