import streamlit as st

st.title("Registration from")

col1 , col2 = st.columns(2)

col1.text_input("First Name",value = "first name")

col2.text_input("Second Name")

email,mob_no=st.columns([3,1])
email.text_input("Enter mail ID")
mob_no.text_input("Enter your mobile number")

user,passw,re_passw=st.columns(3)
user.text_input("Username")
passw.text_input("Enter password",type="password")
re_passw.text_input("Repeat Password",type="password")

button1,button2,button3=st.columns(3)

agree=button1.checkbox("I Agree",value=False)
if button3.button("Submit"):
    if agree:
        st.success("Done")
    else:
        st.warning("Please Check the T&C box")