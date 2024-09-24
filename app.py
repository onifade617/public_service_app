# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:27:47 2024

@author: Awarri User
"""

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Multi-Page Streamlit App", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Page 1", "Page 2"))

# Load the corresponding page
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Multi-Page Streamlit App!")
    st.write("Use the sidebar to navigate to different pages.")
elif page == "Page 1":
    from page1 import display_page
    display_page()
elif page == "Page 2":
    from page2 import display_page
    display_page()