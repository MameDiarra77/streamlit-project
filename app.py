import streamlit as st

st.title("Mon application Streamlit")

if st.button("Say hello", key="btn_hello_1"):
    st.success("Hello ")

if st.button("Say bye", key="btn_bye"):
    st.warning("Bye ")


