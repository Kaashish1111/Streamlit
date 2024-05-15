# How to display text
import streamlit as st
# streamlit provides us with two type of header : a.header and b. subheader
st.title("Hello Streamlit")
st.header("Welcome")
st.subheader("apka hardik sawagt hai")
st.text("hii my name is kashish")
# To format the text
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
#### h4 tag
:moon:<br/>
:girl:
:man:
**This text is bold**
<br/>
_italics_
""",True)    #This is to add emoji :nameOfTheEmoji
# cheatsheet that have all the basic commands in markdwon https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# How to use latex
st.latex("")