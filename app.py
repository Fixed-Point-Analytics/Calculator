import streamlit as st
import pandas as pd
import numpy as np
import nvd3 as nv
import datetime as dt

#Initial page setup

st.set_page_config(
     page_title='ROAS Calculator',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    calc_sidebar()
    calc_body()

    return None


#Sidebar

def calc_sidebar():

    st.header('Control Panel')
    st.text('Seriously show me!!!')

    return None

#Main body

def calc_body():

    st.title('ROAS Calculator')
    st.text('Text')
    
    return None

