nexalytic@nexalytic:~$ cat app.py
import streamlit as st

st.set_page_config(page_title="Nexalytic", layout="centered")
st.title("Nexalytic AI")

api_key = st.text_input("Enter Account API Key", type="password")
if st.button("Login"):
    st.session_state["api_key"] = api_key
    st.success("Authenticated. Proceed to Command Center.")

st.markdown("""
    <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
""", unsafe_allow_html=True)
nexalytic@nexalytic:~$
