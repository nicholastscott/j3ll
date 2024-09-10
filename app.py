import streamlit as st

with st.sidebar:
    st.logo("logos/logo-no-background.png")
    st.title("Built to classify 311 data")
    choice = st.radio("Agency", ["All","Streets Department","Philly311 Contact Center",])
    st.info("This application was designed with the citizen and call center responder in mind. It allows while suggesting: 1. Agency Assignment and 2. Importance/Urgency")


st.write("Hello!")

if choice == "":
    pass