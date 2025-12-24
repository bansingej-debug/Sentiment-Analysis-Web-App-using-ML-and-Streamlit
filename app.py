import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Sentiment Analysis App", layout="centered")

st.title("💬 Sentiment Analysis Web App")
st.write("Analyze sentiment of any sentence using Machine Learning")

# User input
user_input = st.text_area("Enter a sentence to analyze sentiment:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        text_vec = vectorizer.transform([user_input])
        prediction = model.predict(text_vec)[0]

        if prediction == 2:
            st.success("😊 Positive Sentiment")
        elif prediction == 1:
            st.info("😐 Neutral Sentiment")
        else:
            st.error("😠 Negative Sentiment")

s
