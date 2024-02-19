import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Settings"], icons=['house', 'gear'], default_index=1)
    selected
