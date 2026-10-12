import streamlit as st

st.set_page_config(page_title="HTML Test", layout="wide")

st.markdown("""
<div style="background:#172554; padding:30px; border-radius:20px; color:white;">
    <h1>Skillora AI</h1>
    <p>HTML rendering test successful</p>
</div>
""", unsafe_allow_html=True)
