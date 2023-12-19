import streamlit as st
import os

# Streamlit Setup
title = '<p style="font-family:Helvetica; font-size: 35px;"> Prompt Templates </p>'
st.markdown(title, unsafe_allow_html=True)
st.markdown(
    """
    The playground uses a **prompt template for each strategy** that encompasses the specific tactics and examples for that strategy. Given a baseline prompt, the prompt template will return an improved prompt based on the strategy. You can also run the improved prompt to see the response. The prompt templates are stored in an **AIConfig** - a JSON-serializable config to manage prompts, models, and model settings.

    [AIConfig](https://github.com/lastmile-ai/aiconfig) is an open-source framework for building generative AI applications quickly and reliably in production. You can use the AIConfig SDK (model-agnostic) to run prompts from the AIConfig.

    * The AIConfig is setup to run with Gemini, gpt-3.5-turbo, gpt-4, PaLM2.
    * In this playground, the prompt templates are used with gpt-3.5-turbo. See [docs](https://aiconfig.lastmileai.dev/docs/basics) to run with other models.

    Download the AIConfig [here](https://github.com/tanya-rai-lm/streamlit_apps/blob/main/prompt-engineering-guide/openai_prompt_guide.aiconfig.json)
    """
)

file = "../prompt-engineering-guide/openai_prompt_guide.aiconfig.json"
absolute_path = os.path.abspath(file)

code = open(absolute_path, 'r').read()

st.code(code, language='json')
