import stramlit as st
import pandas as pd

st. title("Excel Update App")

df = pd.read_csv("data/names.csv")
st.table(df)

st.sidebar.header("Options")
option.write("Update File")