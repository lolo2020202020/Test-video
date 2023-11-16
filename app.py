import streamlit as st

from Feature_01 import return_even

original_list = [i for i in range(10)]

even_list = return_even(original_list)



st.write("Hooray, we connected everything")

st.write("Ciao")