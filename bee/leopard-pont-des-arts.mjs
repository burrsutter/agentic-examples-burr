import { BeeAgent } from 'bee-agent-framework/agents/bee/agent';
import { OllamaChatLLM } from 'bee-agent-framework/adapters/ollama/chat';
import { OpenAIChatLLM } from 'bee-agent-framework/adapters/openai/chat';
import { TokenMemory } from 'bee-agent-framework/memory/tokenMemory';
import { Ollama } from 'ollama';
import { Agent } from 'undici';
import { DuckDuckGoSearchTool } from 'bee-agent-framework/tools/search/duckDuckGoSearch';

const SHOW_AGENT_PROCESS = false;

const noTimeoutFetch = (input, init) => {
  const someInit = init || {};
  return fetch(input, {
    ...someInit,
    dispatcher: new Agent({ headersTimeout: 2700000 }),
  });
};

const OLLAMA_SERVER = 'http://10.1.2.38:11434';
const MODEL = 'granite3.1-dense';

/////////////////////////////////////
// Ollama
// const llm = new OllamaChatLLM({
//   modelId: MODEL,
//   parameters: {
//     temperature: 0,
//   },
//   client: new Ollama({
//     host: OLLAMA_SERVER,
//     fetch: noTimeoutFetch,
//   }),
// });


const llm = new OpenAIChatLLM({
  baseURL: 'https://api.openai.com/v1',
  apiKey: process.env.API_KEY,
  modelId: "gpt-4o",  
  parameters: {
    max_tokens: 500,
    temperature: 0.1    
  },
});


// Create agent
let agent = new BeeAgent({
  llm,
  memory: new TokenMemory({ llm }),
  tools: [new DuckDuckGoSearchTool()],
});

// Ask a question using the bee agent framework
async function askQuestion(question) {
  const response = await agent
    .run(
      { prompt: question },
      {
        execution: {
          maxRetriesPerStep: 5,
          totalMaxRetries: 5,
          maxIterations: 5,
        },
      },
    )
    .observe(emitter => {
      emitter.on('update', async ({ update }) => {
        if (SHOW_AGENT_PROCESS) {
          console.log(`Agent (${update.key}) 🤖 : `, update.value);
        }
      });
    });

  return response.result.text;
}

console.log(
  await askQuestion(
    'How many seconds would it take for a leopard at full speed to run through Pont des Arts?',
  ),
);
