import streamlit as st


def home_page():

    st.title("Home Page")

    st.markdown("""
    <style>
    /* Set background color */
    .stApp {
        background-color: #f5f5f5;
    }

    /* Style the page title */
    h1 {
        color: #336699;
        text-align: center;
    }

    /* Add padding to the content area */
    .block-container {
        padding: 20px;
    }

    /* Add margin to the top of the page to improve tab visibility */
    .main {
        margin-top: 60px;  # Adjust margin as desired
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    logo_url = "https://static.vecteezy.com/system/resources/previews/026/226/868/non_2x/sentiment-analysis-icon-illustration-vector.jpg"  # Replace with your logo URL
    logo_url1 = "https://cdn3.iconfinder.com/data/icons/2018-social-media-logotypes/1000/2018_social_media_popular_app_logo_twitter-512.png"  # Replace with your logo URL

    with col1:
        st.image(logo_url, width=100)

    with col2:
        st.image(logo_url1, width=100)


    st.markdown("""
    ## Welcome to the Home Page of the Sentiment Analyzer App!

    This app allows you to predict the sentiment of tweets. You can navigate to the 'Sentiment Analyzer' tab to use the tool.

    Enjoy your time using the app!
    """)
