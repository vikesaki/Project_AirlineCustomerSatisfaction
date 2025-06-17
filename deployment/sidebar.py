import streamlit as st

def render_sidebar():
    st.sidebar.title("Airline Customer Satisfaction Project")
    st.sidebar.markdown("Explore airline passenger satisfaction through interactive visualizations and machine learning.")
    st.sidebar.markdown("This dashboard allows you to examine patterns in flight delays, service ratings, and customer feedback.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Navigation")
    selected = st.sidebar.radio("Go to", ["Home", "Exploratory Data Analysis", "Prediction"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("a project by *[vikesaki](github.com/vikesaki)*")
    
    return selected

