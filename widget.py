import streamlit as st

st.title("Widgets")
if st.button("like"):
    st.write("you like this")

name=st.text_input("Name")
description=st.text_area("About Me")
st.write("Hello",name)

date=st.date_input("Enter Date")
time=st.time_input("Enter Time")

if st.checkbox("You accept all cokkies",value=False):   # here we wrote value=false means by default it would be false
    st.write("Thank you")

value1=st.radio("Fruits",["Orange","Apple","Mango"])
value2=st.selectbox("Fruits",["Orange","Apple","Mango"])

values=st.multiselect("Fruits",["Orange","Apple","Mango"])
st.write(values)

# adding a slider
st.slider("marks",max_value=30,value=11)

number=st.number_input("numbers",max_value=60.0,value=0.0) # either in float or number

# file uploader
file=st.file_uploader("Upload your file")
if file is not None:
    st.image(file)