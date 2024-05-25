import streamlit as st

st.title("Widgets")
if st.button("like"):
    st.write("you like this")

name=st.text_input("Name")
description=st.text_area("About Me")
st.write("Hello",name)