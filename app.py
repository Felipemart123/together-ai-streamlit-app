import os
import streamlit as st
import together

# Pull the Together API key from Streamlit secrets
together.api_key = os.getenv("TOGETHER_API_KEY")

st.set_page_config(page_title="Together AI Code Generator", page_icon="🛠️")

st.title("🛠️ Together AI • Python Code Generator")

prompt = st.text_area(
    "Describe the Python code you want to generate:",
    placeholder="e.g. Write a Python script to reverse a string."
)

generate = st.button("Generate code")

if generate and prompt.strip():
    with st.spinner("Thinking..."):
        resp = together.Complete.create(
            model="togethercomputer/llama-2-7b-chat",  # ✅ Changed the model to one that accepts simple prompts
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
            top_p=0.7,
        )
        code = resp['output']['choices'][0]['text'].strip()

    st.subheader("Generated code")
    st.code(code, language="python")
