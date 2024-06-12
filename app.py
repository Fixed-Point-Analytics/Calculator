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

def calc_sidebar(CostPerConversion, HaloPercent, StartDate, EndDate):

    st.sidebar.header('Control Panel')
    st.sidebar.text('Seriously show me!!!')
    CostPerConversion = st.sidebar.number_input('Enter the estimated cost per conversion or enrollment', value=0)
    HaloPercent = st.sidebar.number_input('Enter in the estimated halo effect as a percentage', value=0)
    StartDate = st.sidebar.date_input('Enter the start date of the campaign', value=dt.date.today())
    EndDate = st.sidebar.date_input('Enter the end date of the campaign', value=dt.date.today())

    st.write("Cost per conversion: ", CostPerConversion)
    st.write("Halo effect: ", HaloPercent)
    st.write("Start date: ", StartDate)
    st.write("End date: ", EndDate)


    return CostPerConversion, HaloPercent, StartDate, EndDate

#Main body

def calc_body(CostPerConversion, HaloPercent, StartDate, EndDate):

    st.title('ROAS Calculator')
    st.text('Text')

    st.write("Cost per conversion: ", CostPerConversion)
    st.write("Halo effect: ", HaloPercent)
    st.write("Start date: ", StartDate)
    st.write("End date: ", EndDate)

    
    return None

# Run main()

if __name__ == '__main__':
    main()