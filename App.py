import streamlit as st

st.set_page_config(
    page_title="HOME",
   # page_icon="👋",
)

# css styling [style.css]
with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.subheader('Papua New Guinea National Weather Service')
st.write("# Climatology")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)