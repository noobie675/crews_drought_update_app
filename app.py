import streamlit as st
from drought import *
from home import *

# css styling [style.css]
with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## Navigation")
with st.sidebar.container():
   genre = st.radio(
    "Go to",
    ('Home', 'PNG CREWS', 'Products'))


if genre == 'Home':
     pg_home()
elif genre == 'PNG CREWS':
    col1, col2 ,col3 = st.columns(3)
    option1 = col1.selectbox('Select Month',
     ('April', 'March', 'February'))

    data = './file/drought_template June.pdf'
    col3.text('Get the PDF version')
    col3.download_button('Download Outlook', data)
    mon = option1
    yr = 2022
    dr_update(mon)
else:
    st.title('PAGE UNDER CONSTRUCTION')

