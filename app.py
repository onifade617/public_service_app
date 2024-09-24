# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:27:47 2024

@author: Awarri User
"""

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Multi-Page Streamlit App", layout="wide")

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar for navigation
st.sidebar.title("Navigation")

# Create buttons for navigation
if st.sidebar.button("Home"):
    st.session_state.page = 'home'
if st.sidebar.button("Federal Fire Service"):
    st.session_state.page = 'fire service'
if st.sidebar.button("Nigeria Security & Civil Defence Corps"):
    st.session_state.page = 'NSCDC'
if st.sidebar.button("Nigeria Correctional Service Center"):
    st.session_state.page = 'NCS'

# Display the selected page
if st.session_state.page == 'home':
    st.title("Home Page")
    st.write("Welcome to the Multi-Page Streamlit App!")
    st.write("Use the sidebar to navigate to different pages.")
elif st.session_state.page == 'fire service':
    from page1 import display_page as fire
    fire()
elif st.session_state.page == 'NSCDC':
    from page2 import display_page as civil_defence
    civil_defence()
elif st.session_state.page == 'NCS':
    from page3 import display_page as correction
    correction()
