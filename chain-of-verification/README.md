# Chain-of-Verification Demo

This streamlit app shows chain-of-verification with AIConfig. \n
Check out AIConfig here: https://github.com/lastmile-ai/aiconfig\n

Instructions:\n
Go to https://cove.streamlit.app/. \n
Requires OpenAI Key with GPT-4 accesss. https://platform.openai.com/account/api-keys \n

1. Generate a Baseline Response - Ask ChatGPT to generate a numbered list of 10-20 facts. Follow the format below. \n
Examples:\n
Name 15 celebrities born in Toronto, Canada.\n
Name 20 programming languages developed in the United States.\n
Name 15 politicians born in New York City.\n

3. Ask a verification question to validate each entity in the baseline response.\n
Examples:\n
Where was this celebritity born?\n
Where was this programming language developed?\n
Where was this politician born?\n

5. Chain-of-Verification Pipeline Runs!\n
Now, you should see the revised results of the baseline response given the validation of facts from Step 2.\n
