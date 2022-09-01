import streamlit as st
from drought import *

st.title("PNG CREWS Drought Update")
mon = 'April'
yr = 2022
dr_update(mon, yr)
