import streamlit as st
from aiconfig import AIConfigRuntime

# Streamlit Setup
st.title("AI Config ⚙️")
st.text(
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
        Download this AIConfig to use in your own application.
        You can use the SDK to connect AIConfig to your application code. Github: [link]
    """
)
path = "assistant_aiconfig.json"
code = open(path, 'r').read()

st.code(code, language='json')