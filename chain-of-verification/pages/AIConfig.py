import streamlit as st
import os

# Streamlit Setup
st.title("AIConfig ⚙️")
st.markdown(
    """
        AIConfig is a standardized JSON format to store prompts and model settings in source control.
        This is an AI artifact that can easily be used across any application.
        Use the Python or Node SDK to connect an AIConfig to your application code. Github: [link](https://github.com/lastmile-ai/aiconfig).
    """
)

file = "../chain-of-verification/cove_aiconfig.json"
absolute_path = os.path.abspath(file)

code = open(absolute_path, 'r').read()

st.code(code, language='json')
