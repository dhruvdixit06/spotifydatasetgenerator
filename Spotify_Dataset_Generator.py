import streamlit as st

st.set_page_config(page_title="About", page_icon="🎶",layout="wide",)

st.header('About Spotify Dataset Generator')
about= '''
Whenever creating an app or a software, dataset is the most required thing for researches, data analysis, building models, recommendation systems etc. 
\nThis tool is helpful to all the creators dedicated to music and are in need of Dataset generated via Spotify.
'''
st.markdown(about,unsafe_allow_html=True)

st.header('About Developer')
d='''
Made with ❤️ by Dhruv Dixit \n
Github : https://github.com/dhruvdixit06 \n
LinkedIn : https://www.linkedin.com/in/dhruv-dixit/
'''
st.markdown(d,unsafe_allow_html=True)
