import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Dispay Title and Description
st.title("Fridge")
st.markdown("Enter the product below")

#Establishing a Google Sheets Connection
conn = st.experimental_conncection("gseets", type=GSheetsConnection)

#Fetch existing product data
existing_data = conn.read(worksheet="Products", usecols=list(range(2)), ttl5)
existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)