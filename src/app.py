import sys
from pathlib import Path

import streamlit as st


project_root = str(Path(__file__).parent.parent.absolute())
if project_root not in sys.path:
    sys.path.append(project_root)


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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    ':bust_in_silhouette: Profile Info',
    ':globe_with_meridians: Social Accounts',
    ':memo: Description',
    ':computer: Skills',
    ':heavy_plus_sign: Extensions'
])

from src.github_profile import generate_profile
from src.sections import (personal_info, social_info, description, skills, extensions)

kwargs = {}
kwargs = personal_info(tab1, **kwargs)
kwargs = social_info(tab2, **kwargs)
kwargs = description(tab3, **kwargs)
kwargs = skills(tab4, **kwargs)
kwargs = extensions(tab5, **kwargs)

st.header('README.md Preview')

theme = Path('src/themes/default').name

profile = generate_profile(theme, **kwargs)

tab1, tab2 = st.tabs(['Preview', 'Code'])
tab1.markdown(profile)

with tab2:
    'Copy the code below and paste it in your README.md file'
    st.code(profile)



