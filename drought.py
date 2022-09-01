# template for the crews drought update
import streamlit as st

def dr_update(month,yr):
    up_month = month
    up_year = str(yr)
    up_header = st.header(up_month + ' ' + up_year)
    
    data = './file/drought_template June.pdf'
    st.download_button('Download Outlook', data)

    sec1_head = st.subheader('Key Messages')
    sec1_text = st.write('New Ireland no longer at Drought Alert, however Drought Watch remains active across most north-eastern provinces that experienced severe rainfall deficiency in the past months. East New Britain was most at risk in February.')
    #up_subheader1 = (sec1_head, sec1_text)

    sec2_head = st.subheader('Drought Early Warning Status')
    sec2_text = st.write('Derived from observed rainfall and vegetation health; and forecasted rainfall.')
    #up_subheader2 = (sec2_head, sec2_text)

    col1, col2 = st.columns(2)
    col1.image('./img/vhi_april2022.png')
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
    #up_subheader2 = (sec2_head, sec2_text)
    """
    ### Drought Risk Status
    An indication of past drought risk based on drought hazard, exposure and vulnerability.
    + East New Britain is still at a high-risk level as it has been in recent months; it should be closely monitored.
    + Some provinces are at the Extreme risk level; East New Britain 
    """

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
    
    """
    ### CLimate Context
    A summary of the relevant climate drivers affecting PNG over the coming months
    + ACCESS-S outlooks suggest a wet signal over the south of the mainland for May, becoming more widespread from June onwards.
    + La Niña is expected to end during May, with ENSO returning to neutral.
    + There is the possibility of the development of a negative IOD from June onwards, but model skill is very low at this time of the year. Skill sharply increases from late May onwards.
    """
    d_footer = '<p style="font-size:12px;position:absolute;bottom:-200px;">For more information, feel free to contact the Climate and Special Services team at the PNG-NWS via 3255925 or kinape70@gmail.com</p>'
    st.markdown(d_footer, unsafe_allow_html=True)
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)