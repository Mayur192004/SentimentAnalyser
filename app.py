import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = PorterStemmer()

tfidf_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
loaded_model = pickle.load(open('train.sav', 'rb'))

def stemming(text):

    stemmed_text = re.sub('[^a-zA-Z]', ' ', text).lower()


    stemmed_text = [stemmer.stem(word) for word in stemmed_text.split()]


    return ' '.join(stemmed_text)

def sentiment_analyzer():

    st.title("Sentiment Analyzer")

    input_tweet = st.text_input("Enter the tweet/post message")


    if st.button('Predict'):

        transformed_tweet = stemming(input_tweet)


        vector_input = tfidf_vectorizer.transform([transformed_tweet])


        prediction = loaded_model.predict(vector_input)
        if prediction[0] == 1:
            st.header("Positive Tweet")
        else:
            st.header("Negative Tweet")
