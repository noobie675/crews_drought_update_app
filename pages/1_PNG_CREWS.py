import streamlit as st
import time

st.set_page_config(page_title="CREWS_PNG", page_icon="📈")

padding_top = 2

st.markdown(f"""
    <style>
        div.block-container.css-12oz5g7.egzxvld2{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

def dr_update(month):

    st.header("Drought Update 2022")
    up_month = month
    up_header = st.header(up_month)

    sec1_head = st.subheader('Key Messages')
    sec1_text = st.write('New Ireland no longer at Drought Alert, however Drought Watch remains active across most north-eastern provinces that experienced severe rainfall deficiency in the past months. East New Britain was most at risk in February.')
    #up_subheader1 = (sec1_head, sec1_text)

    sec2_head = st.subheader('Drought Early Warning Status')
    sec2_text = st.write('Derived from observed rainfall and vegetation health; and forecasted rainfall.')
    #up_subheader2 = (sec2_head, sec2_text)

    col1, col2 = st.columns(2)
    col1.image('./img/3dri_april2022.png')
    col2.write(" + March rainfall was notably below average for most provinces except Central Gulf, Southern Highlands and Western.\n + January–March rainfall was below average across provinces in the PNG highlands and in New Ireland, East/West New Britain and Bougainville which is contributing to the drought watch status for these provinces. \n + March vegetation health conditions remain similar to February with some mild vegetation stress present over New Ireland, East New Britain, Bougainville and parts of the PNG Highlands. \n + At the 6-month timescale, East New Britain, Bougainville and New Ireland remain drought affected.")
    
    col1, col2 ,col3 = st.columns(3)
    d_watch = '<p style="color:yellow;font-size:18px">Drought Watch</p>'
    col1.markdown(d_watch, unsafe_allow_html=True)
    col1.markdown("""
    Bougainville, Central, Chimbu, East New Britain, Eastern Highlands, Enga, Hela, Jiwaka, Morobe, NCD, New Ireland, West Sepik,
    """)
    d_alert = '<p style="color:orange;font-size:18px">Drought Alert</p>'
    col2.markdown(d_alert, unsafe_allow_html=True)
    col2.markdown("""
    None
    """)
    d_critical = '<p style="color:red;font-size:18px">Drought Critical</p>'
    col3.markdown(d_critical, unsafe_allow_html=True)
    col3.markdown("""
    None
    """)

    sec3_head = st.subheader('Drought Risk Status')
    sec3_text = st.write('An indication of past drought risk based on drought hazard, exposure and vulnerability.\n+ East New Britain is still at a high-risk level as it has been in recent months; it should be closely monitored.\n+ Some provinces are at the Extreme risk level; East New Britain')
    #up_subheader3 = (sec3_head, sec3_text)

    col1, col2 ,col3 = st.columns(3)
    col1.markdown("""
    #### January 2022
    """)
    col1.image('./img/jan_april2022.png')
    col2.markdown("""
    #### February 2022
    """)
    col2.image('./img/feb_april2022.png')

    col3.markdown("""
    #### March 2022
    """)
    col3.image('./img/mar_april2022.png')
    
    sec4_head = st.subheader('Climate Context')
    sec4_text = st.write('A summary of the relevant climate drivers affecting PNG over the coming months\n+ ACCESS-S outlooks suggest a wet signal over the south of the mainland for May, becoming more widespread from June onwards.\n+ La Niña is expected to end during May, with ENSO returning to neutral.\n+ There is the possibility of the development of a negative IOD from June onwards, but model skill is very low at this time of the year. Skill sharply increases from late May onwards.')
    #up_subheader4 = (sec4_head, sec4_text)
st.sidebar.header("Climate Risk and Early Warning Systems (CREWS)")

with st.sidebar.container():
   genre = st.radio(
    "Projects",
    ('Drought Update',))

if genre == 'Drought Update':
    col1, col2 ,col3 = st.columns(3)
    option1 = col1.selectbox('Select Month',
     ('April', 'March', 'February'))
    data = './file/drought_template June.pdf'
    col3.text('Get the PDF version')
    col3.download_button('Download Outlook', data)
    mon = option1
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