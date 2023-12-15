# Chain-of-Verification Demo

This streamlit app shows chain-of-verification with [AIConfig](https://github.com/lastmile-ai/aiconfig). 

Instructions:
Go to https://cove.streamlit.app/.
Requires OpenAI Key with [GPT-4 accesss](https://platform.openai.com/account/api-keys).

1. Generate a Baseline Response - Ask ChatGPT to generate a numbered list of 10-20 facts. Follow the format of these examples. Examples: Name 15 celebrities born in Toronto, Canada., Name 20 programming languages developed in the United States., Name 15 politicians born in New York City.

3. Ask a verification question to validate each entity in the baseline response. Examples: Where was this celebrity born?, Where was this programming language developed?, Where was this politician born?

5. Chain-of-Verification Pipeline Runs! Now, you should see the revised results of the baseline response given the validation of facts from Step 2.
