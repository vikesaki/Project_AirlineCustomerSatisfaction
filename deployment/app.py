import streamlit as st
import pandas as pd
import numpy as np
import sidebar as sd
import eda
import prediction 
import mainapp 

# Set page config
st.set_page_config(page_title="Airline Satisfaction Dashboard", layout="wide", initial_sidebar_state="expanded")
page = sd.render_sidebar()

if page == "Home":
    mainapp.show()
if page == "Exploratory Data Analysis":
    eda.show()
elif page == "Prediction":
    prediction.show()

