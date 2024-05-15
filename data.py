import streamlit as st
import pandas as pd
import numpy as np
a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape((2,4))
dic={
    "name":"Kashish",
    "age":18,
    "Topic":"Streamlit"
}
data=pd.read_csv("data//Salary_Data.csv")
# print(data)

# st.dataframe(n)
st.dataframe()
st.dataframe(nd)