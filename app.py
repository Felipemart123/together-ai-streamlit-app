import os
import streamlit as st
import together

# Pull the key you’ll add as a Streamlit secret
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
        # Pick any Together model that speaks Python well
        resp = together.Complete.create(
            prompt=prompt,
            model="togethercomputer/CodeLlama-34b-Instruct",
            temperature=0.2,
            max_tokens=300,
        )
        code = resp["choices"][0]["text"].strip()
    st.subheader("Generated code")
    st.code(code, language="python")
