# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:28:25 2024

@author: Awarri User
"""

import streamlit as st
import streamlit as st
import pandas as pd
import pydeck as pdk

def display_page():
    st.title('Federal Fire service Facilities in Lagos State')
    st.write(
    """This app analyzes the Facilities of  Federal Fire service in Lagos """)
    # Load data
    trees_df = pd.read_csv("Fire-Stations.csv")
    trees_df.dropna(how='any', inplace=True)

    # Set the initial view state to Lagos, Nigeria
    lagos_initial_view = pdk.ViewState(
        latitude=6.5244,  # Center of Lagos
        longitude=3.3792,
        zoom=10,          # Adjust the zoom level as needed
        pitch=0
    )
    # Create the scatter plot layer
    sp_layer = pdk.Layer(
        'ScatterplotLayer',
        data=trees_df,
        get_position='[Longitude, Latitude]',  # Ensure correct ordering
        get_radius=30,
        get_fill_color=[255, 0, 0, 160],  # Red with some transparency
    )
   
    # Render the map
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=lagos_initial_view,
        layers=[sp_layer]
    ))
    







