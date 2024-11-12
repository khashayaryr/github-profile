import streamlit as st

def personal_info(tab, **kwargs):
    """

    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['name'] = col1.text_input('name')
        kwargs['email'] = col2.text_input('email')

    return kwargs


def social_info(tab, **kwargs):
    """

    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['linkedin'] = col1.text_input('LinkedIn')
        kwargs['website'] = col2.text_input('Website')
        kwargs['instagram'] = col1.text_input('Instagram')
        kwargs['twitter'] = col2.text_input('Twitter')

    return kwargs


def description(tab, **kwargs):

    with tab:
        st.write("Write a brief description about yourself.")
        kwargs['description'] = st.text_area('Description', height=300)

    return kwargs


def skills(tab, **kwargs):
    with tab:
        st.write("Write your skills. Enter each one into a new line")
        col1, col2 = st.columns(2)
        kwargs['skills'] = col1.text_area('Skills:', height=300)
        kwargs['skills'] = kwargs['skills'].split('\n')
        kwargs['skills'] = filter(lambda x: x, kwargs['skills'])
        kwargs['skills'] = [f'- {skill}' for skill in kwargs['skills']]
        kwargs['skills'] = '\n'.join(kwargs['skills'])

    return kwargs
