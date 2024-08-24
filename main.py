import streamlit as st
from Home import home_page
from app import sentiment_analyzer


tabs = st.tabs(["Home Page", "Sentiment Analyzer"])


with tabs[0]:
    home_page()

with tabs[1]:
    sentiment_analyzer()
