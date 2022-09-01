import streamlit as st
from drought import *


# css styling [style.css]

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.title("PNG CREWS Drought Update")
mon = 'April'
yr = 2022
dr_update(mon, yr)
