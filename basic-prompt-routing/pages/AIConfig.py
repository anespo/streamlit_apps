import streamlit as st
import os

# Streamlit Setup
st.title("AI Config ⚙️")
st.markdown(
    """
        AIConfig saves prompts, models and model parameters as source-controlled configs. 
        This is your generative AI artifact that can easily be shared across any application.
        Use our SDK to connect an AIConfig to your application code. The separation of the generative
        AI components from your application code reduces complexity, increase iteration, and promotes
        better collaboration.
    """
)
st.markdown(
    """
        Download this AIConfig to use in your own application. [link](https://github.com/tanya-rai-lm/streamlit_apps/blob/main/basic-prompt-routing/assistant_aiconfig.json) \n
        You can use the SDK to connect AIConfig to your application code. Github: [link](https://github.com/lastmile-ai/aiconfig)
    """
)

file = "../streamlit_apps/basic-prompt-routing/assistant_aiconfig.json"
absolute_path = os.path.abspath(file)

code = open(absolute_path, 'r').read()

st.code(code, language='json')
