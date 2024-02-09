import streamlit as st
from joblib import load
import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import gradio as gr

gr.load("models/gyro5/dialo-bot").launch()
# Load the model and vectorizer
nb_model = load('nb_model.joblib')
tfidf_vectorizer = load('tfidf_vectorizer.joblib')

# Load intent_data.json
with open('intent_data.json', 'r') as file:
    intent_data = json.load(file)

# Function to preprocess text
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(lemmatized_text)

# Function to fetch response based on predicted intent
def get_response(predicted_intent):
    for item in intent_data:
        if item['tag'] == predicted_intent:
            return item['responses'][0]  # Assuming each intent has at least one response
    return "Sorry, I can't help with that."

# Streamlit app
def main():
    st.title("Chatbot Naive Bayes")

    user_input = st.text_area("Hi, how may I help you? :)", "")

    if st.button("Send"):
        preprocessed_input = preprocess_text(user_input)
        transformed_input = tfidf_vectorizer.transform([preprocessed_input])
        prediction = nb_model.predict(transformed_input)
        predicted_intent = prediction[0]
        response = get_response(predicted_intent)
        st.write(f"Response: {response}")

if __name__ == "__main__":
    main()
