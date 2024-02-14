
import streamlit as st
import pandas as pd
st.title("Welcome Bano Qabil")

#creating dataset

df=pd.DataFrame({'first':[1,2,3,4,5,],'second':[6,7,8,9,10]})
st.write(df)

# or
df  #magic comments
st.area_chart(df)
st.sidebar.bar_chart(df)
