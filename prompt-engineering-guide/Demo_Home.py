import asyncio
import os
import re
import openai
import streamlit as st
from aiconfig import AIConfigRuntime

# streamlit page setup
st.set_page_config(
    page_title="OpenAI Prompt Engineering Playground 🧪💫",
    page_icon="㏐",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
title = '<p style="font-family:Helvetica; font-size: 35px;"> OpenAI Prompt Engineering Playground </p>'
st.markdown(title, unsafe_allow_html=True)
st.markdown(
    """
    The [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results) is a game changer for improving your prompts.

    This playground is a companion to the official guide. You can enter a prompt and experiment on improving the prompt with the different strategies. The prompt templates for each of the strategies is accessible to you via a JSON-serializable config called 
    [AIConfig](https://github.com/lastmile-ai/aiconfig).
    """
)
strategy_dict = {
    "Write clearer instructions": "clear_instructions",
    "Provide reference text": "provide_ref_text",
    "Split complex tasks into simpler subtasks": "split_into_subtasks",
    "Give the model time to 'think'": "model_think_first",
    "Test changes systematically": "systematic_testing"
}

openai_api_key = st.text_input("Enter you OpenAI API Key to begin. Requires GPT-4:  🔑", type="password")

# playground setup
async def playground():
    st.markdown("#### ➡️ Step 1: Enter a prompt")
    
    if 'original_prompt' not in st.session_state:
        st.session_state.original_prompt = ""
        
    st.session_state.original_prompt = st.text_input(label="This is your baseline prompt", value=st.session_state.original_prompt, placeholder="Ex:  write a satirical poem on AI")

    if st.session_state.original_prompt:
        st.markdown("#### ➡️ Step 2: Select a Strategy from the Guide")
        
        selection = st.selectbox("Experiment with one of the strategies from the guide", ["Select an option", "Write clearer instructions", "Provide reference text", "Split complex tasks into simpler subtasks", "Give the model time to 'think'", "Test changes systematically"])
        
        if selection in strategy_dict:
            await config.run(strategy_dict[selection], params = {"original_prompt": st.session_state.original_prompt})
            improved_prompt_details_1 = config.get_output_text(strategy_dict[selection])
            st.markdown(improved_prompt_details_1)
            st.session_state.improved_prompt_details_1 = improved_prompt_details_1

            if st.session_state.improved_prompt_details_1:
                st.markdown("#### ➡️ Step 3: Run the improved prompt")
                if st.button("Run improved prompt"):
                    with st.spinner('Running prompt...'):
                        await config.run("run_improved_prompt", params={"improved_prompt": re.search(r"(?i)Improved Prompt\s*(.*)", st.session_state.improved_prompt_details_1).group(1)})
                    improved_response = config.get_output_text("run_improved_prompt")
                    st.write(improved_response)

# aiconfig setup 
if openai_api_key:
    openai.api_key = openai_api_key
    config = AIConfigRuntime.load(os.path.join(os.path.dirname(__file__), "openai_prompt_guide.aiconfig.json"))
    asyncio.run(playground())
