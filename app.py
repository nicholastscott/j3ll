import streamlit as st

with st.sidebar:
    st.logo("/Users/nicholasscott/Documents/j3ll/logos/logo-no-background.png")
    st.title("Built to classify 311 data")
    choice = st.radio("Navigation", ["","",])
st.write("Hello!")
