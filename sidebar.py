import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import time

# multipage
page=st.sidebar.radio("Navigation",["Home","Shop"])
plt.style.use("ggplot")
data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
df=pd.DataFrame(data = data)
col=st.sidebar.selectbox("Select a column",df.columns)
col=st.sidebar.multiselect("Select a column",df.columns)
plt.plot(df['num'],df[col])
st.pyplot()
if page == "Shop":
    # adding progress bar
    progress=st.progress(0)
    for i in range(0,100):
        time.sleep(0.1)
        progress.progress(1+i)

# ballon animation
    st.balloons()

    st.write("Welcome to Shop page")
    st.error("Error")
    st.success("Show Success")
    st.info("information")
    st.exception(RuntimeError("Careful pron to run time error"))
    st.warning("Warning man careful")