import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Positive 😊")
    elif polarity < 0:
        st.error("Negative 😞")
    else:
        st.info("Neutral 😐")

    st.write("Polarity Score:", polarity)