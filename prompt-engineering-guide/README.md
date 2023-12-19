# OpenAI Prompt Engineering Guide - Prompt Templates

The [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results) is a game changer for improving your prompts. The guide contains 6 key strategies.

The playground uses a **prompt template for each strategy** that encompasses the specific tactics and examples for that strategy. Given a baseline prompt, the prompt template will return an improved prompt based on the strategy. You can also run the improved prompt to see the response. The prompt templates are stored in an **AIConfig** - a JSON-serializable config to manage prompts, models, and model settings.

[AIConfig](https://github.com/lastmile-ai/aiconfig) is an open-source framework for building generative AI applications quickly and reliably in production. You can use the AIConfig SDK (model-agnostic) to run prompts from the AIConfig.

* The AIConfig is setup to run with Gemini, gpt-3.5-turbo, gpt-4, PaLM2.
* In this playground, the prompt templates are used with gpt-4. See [docs](https://aiconfig.lastmileai.dev/docs/basics) to run with the other models.

## Resource
* [Playground (Streamlit App)](https://openai-prompt-guide.streamlit.app/)
* [Google Colab](https://colab.research.google.com/drive/15-0MEu6JyFx0hpF88vShjVmt9wOYmTMe#scrollTo=DRxhxoZHD_Ni)
* [Prompt Templates (aiconfig.json)](https://github.com/tanya-rai-lm/streamlit_apps/blob/main/prompt-engineering-guide/openai_prompt_guide.aiconfig.json)