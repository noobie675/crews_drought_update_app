import streamlit as st
from fpdf import FPDF
import base64
import json

st.set_page_config(page_title="CREWS_PNG", page_icon="📈")

# css styling [style.css]
with open ('./style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Loading schema.json
with open('./schema.json', 'r') as f:
    outlooks = json.load(f)

# scan for the selected month outlook data
def dr_scan(month):
    outlook_months = outlooks['outlooks']
    for mon in outlook_months:
        if mon['month'] == month:
            return mon
    return False

def dr_update(month):
    with st.spinner(text='In progress'):
        up_month = dr_scan(month)

    def looper(arr, col = None):
        if col :
            for a in arr:
                col.markdown('+ ' + a)
        else:
            markdown('+ ' + a)
    
    header = outlooks['header'] + ' ' + up_month['year']
    st.header(header)
    
    st.header(up_month['month'])
    issued_date = up_month['date_issued']
    issued_date = '<p style="color:white;font-size:12px;padding-top:0px">date issued: '+issued_date+'</p>'
    st.markdown(issued_date, unsafe_allow_html=True)

    sec1_head = st.subheader('Key Messages')
    sec1_text = st.write(up_month['key_messages'])
    #up_subheader1 = (sec1_head, sec1_text)

    sec2_head = st.subheader('Drought Early Warning Status')
    sec2_text = st.write('Derived from observed rainfall and vegetation health; and forecasted rainfall.')
    #up_subheader2 = (sec2_head, sec2_text)
    col1, col2 = st.columns(2)
    col1.image('./img/3dri_april2022.png')
    looper(up_month['drought_EW_status']['points'],col2)
    
    
    col1, col2 ,col3 = st.columns(3)
    ## drought watch
    d_watch = '<p style="color:yellow;font-size:18px">Drought Watch</p>'
    col1.markdown(d_watch, unsafe_allow_html=True)
    col1.markdown(up_month['drought_EW_status']['drought_summary']['watch'])

    ## drought alert
    d_alert = '<p style="color:orange;font-size:18px">Drought Alert</p>'
    col2.markdown(d_alert, unsafe_allow_html=True)
    col2.markdown(up_month['drought_EW_status']['drought_summary']['alert'])
    ## drought critical
    d_critical = '<p style="color:red;font-size:18px">Drought Critical</p>'
    col3.markdown(d_critical, unsafe_allow_html=True)
    col3.markdown(up_month['drought_EW_status']['drought_summary']['critical'])

    sec3_head = st.subheader('Drought Risk Status')
    sec3_text = st.write('An indication of past drought risk based on drought hazard, exposure and vulnerability.')
    looper(up_month['drought_R_status']['points'],st)
    #up_subheader3 = (sec3_head, sec3_text)

    col1, col2 ,col3 = st.columns(3)
    col1.subheader(up_month['drought_R_status']['data']['dr_header'][0] + ' ' + up_month['year'])
    col1.image('./img/jan_2022.png')

    col2.subheader(up_month['drought_R_status']['data']['dr_header'][1] + ' ' + up_month['year'])
    col2.image('./img/feb_2022.png')

    col3.subheader(up_month['drought_R_status']['data']['dr_header'][2] + ' ' + up_month['year'])
    col3.image('./img/mar_2022.png')
    
    sec4_head = st.subheader('Climate Context')
    sec4_text = st.write('A summary of the relevant climate drivers affecting PNG over the coming months.')
    looper(up_month['climate_context']['points'],st)
    #up_subheader4 = (sec4_head, sec4_text)


def pdf_download(mnth, col):
    month = dr_scan(mnth)
    pdf_path = month['pdf_path']

    with open(pdf_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    pdf_name = month['month'] + month['year'] + '_' + outlooks['header']
    col.download_button(label="Download Outlook",
                    data=PDFbyte,
                    file_name= pdf_name + ".pdf",
                    mime='application/octet-stream')


st.sidebar.header("Climate Risk and Early Warning Systems (CREWS)")

with st.sidebar.container():
   genre = st.radio(
    "Projects",
    ('Drought Update',))

if genre == 'Drought Update':
    col1, col2 ,col3 = st.columns(3)
    option1 = col1.selectbox('Select Month',
     ('August', 'June'))
    col3.text('Get the PDF version')
    mon = option1
    pdf_download(mon,col3)
    dr_update(mon)
else:
    st.title('PAGE UNDER CONSTRUCTION')

d_footer = '<p style="font-size:12px;position:absolute;bottom:-200px;">For more information, feel free to contact the Climate and Special Services team at the PNG-NWS via 3255925 or kinape70@gmail.com</p>'
st.markdown(d_footer, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)