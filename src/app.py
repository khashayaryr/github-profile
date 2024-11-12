import sys
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="GitHub Profile Generator",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get help' : "mailto: khashayar.yavari@gmail.com",
        'Report a bug': "https://github.com/khashayaryr/github-profile",
        'About': "This is built by Khashayar Yavari with the help of [Pytopia](pytopia.ai) courses"
        }
)

st.title(':page_with_curl: Github Profile Readme Generator')



st.header('Personalize your Readme')
tab1, tab2, tab3, tab4 = st.tabs([
    ':bust_in_silhouette: Profile Info',
    ':globe_with_meridians: Social Accounts',
    ':memo: Description',
    ':computer: Skills',
])

with tab1:
    col1, col2 = st.columns(2)
    name = col1.text_input('name')
    email = col2.text_input('email')

st.header('README.md Preview')


tab1, tab2 = st.tabs(['Preview', 'Code'])
tab1.markdown("profile")

with tab2:
    'Copy the code below and paste it in your README.md file'
    st.code("profile")



