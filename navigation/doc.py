import streamlit as st

from texts.descriptions import Desc
from .home import TITLE
import hydralit_components as hc


option_data = [
   {'icon': "", 'label':i} for i in ['Introduction', 'Usage', 'Database Implementation']]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'green'}
font_fmt = {'font-class':'h3','font-size':'50%'}


# display a horizontal version of the option bar



def doc_page():
    page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        # font_styling=font_fmt,
        horizontal_orientation=True)
    
    if page == 'Introduction':
        st.header('Introduction')
        st.write(Desc.manuscript_intro)
        
        with st.expander("Data Collection and Processing", expanded=True):
            st.image('./assets/images/documentation.png')
        
        
        
        # st.header('SPaRTAN')
        # st.write(Desc.spartan)
        
        with st.expander("Model Overview"):
            st.write(Desc.spartan_model)
            st.image('./assets/images/SPaRTAN_fig.png')
        

    elif page == 'FAQ':
        # st.header('How to cite')
        st.image('./assets/images/under_construction.png')        
        
            
            
    elif page == 'Usage':
        st.caption(f'Example usage of the {TITLE}')
        video_file = open('./assets/video/video.webm', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
    
    elif page == 'Database Implementation':
        # st.header(f'Detailed implementation of the {TITLE}')
        st.image('./assets/logos/tech.png')
        st.subheader('Backend implementation')
        st.write("""
        We build the COVID-19db of Immune Cell States web portal to present the analysis results in a user-friendly way. All the processed and annotated datasets can be searched, visualized and downloaded from the web portal. The backend of the portal was implemented in Python (version: 3.9.13), while the frontend is written in TypeScript via the Streamlit open-source framework. All the charts are generated by in-house Python and R scripts. All the functions of the database have been tested in Google Chrome and Apple Safari browsers. Static figures and logos were made using Biorender.
        """)
        
        st.markdown('---')
        
        st.subheader("Statistical analysis and visualization")
        st.write(Desc.analysis)
        
        st.markdown('---')
        
        st.subheader("Cell-type specific SPaRTAN models")
        st.write(Desc.doc_spartan)
        
        st.markdown('---')
        
        
        # st.subheader('Data Availability')
        st.subheader('Code Availability')
        st.write('All the code for the database are available at https://github.com/osmanbeyoglulab/covid19_webapp')
        st.write("""Apache License 2.0""")
        
        st.markdown('---')
        st.subheader("Funding")
        st.write("""This study was funded by support from the National Institutes of Health (R35GM146989).""")
        
    
        