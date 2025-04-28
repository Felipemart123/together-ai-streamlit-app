import os
import streamlit as st
import together

# Load Together API Key
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
            model="togethercomputer/CodeGen-2B-mono",  # <--- simple model
            prompt=prompt,
            max_tokens=256,
            temperature=0.5,
            top_p=0.7,
        )
        code = resp['output']['choices'][0]['text'].strip()
        
    st.subheader("Generated code")
    st.code(code, language="python")
