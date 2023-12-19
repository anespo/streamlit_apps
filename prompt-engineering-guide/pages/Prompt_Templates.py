import streamlit as st
import os

# Streamlit Setup
st.title("Prompt Templates ⚙️")
st.markdown(
    """
    The playground uses a **prompt template for each strategy** that encompasses the specific tactics and examples for that strategy. Given a baseline prompt, the prompt template will return an improved prompt based on the strategy. You can also run the improved prompt to see the response. The prompt templates are stored in an **AIConfig** - a JSON-serializable config to manage prompts, models, and model settings.

    [AIConfig](https://github.com/lastmile-ai/aiconfig) is an open-source framework for building generative AI applications quickly and reliably in production. You can use the AIConfig SDK (model-agnostic) to run prompts from the AIConfig.

    * The AIConfig is setup to run with Gemini, gpt-3.5-turbo, gpt-4, PaLM2.
    * In this playground, the prompt templates are used with gpt-4. See [docs](https://aiconfig.lastmileai.dev/docs/basics) to run with other models.
    * See the Google Colab version of this playground [here](https://colab.research.google.com/drive/15-0MEu6JyFx0hpF88vShjVmt9wOYmTMe#scrollTo=fLpCYI-Gt-9Q)
    """
)

file = "../prompt-engineering-guide/openai_prompt_guide.aiconfig.json"
absolute_path = os.path.abspath(file)

code = open(absolute_path, 'r').read()

st.code(code, language='json')
