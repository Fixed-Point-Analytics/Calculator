import streamlit as st
import pandas as pd
import numpy as np
import nvd3 as nv
import datetime as dt

#Initial page setup

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    calc_sidebar()
    calc_body()

    return None


#Sidebar

def calc__sidebar():

    st.sidebar.title('Sidebar')
    st.sidebar.subheader('Subheader')
    st.sidebar.text('Text')
    st.sidebar.markdown('Markdown')

    return None

#Main body

def calc_body():

    st.title('Title')
    st.header('Header')
    st.subheader('Subheader')
    st.text('Text')
    st.markdown('Markdown')

    return None
