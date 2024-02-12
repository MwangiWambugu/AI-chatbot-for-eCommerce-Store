import streamlit as st
from joblib import load
import pandas as pd

# Load the model and vectorizer
nb_model = load('nb_model.joblib')
tfidf_vectorizer = load('tfidf_vectorizer.joblib')

# Streamlit webpage
def main():
    st.title("Text Classification with Multinomial Naive Bayes")

    # User input
    user_input = st.text_area("Enter text here", "")

    # Predict button
    if st.button("Predict"):
        # Transform the user input
        transformed_input = tfidf_vectorizer.transform([user_input])
        
        # Make a prediction
        prediction = nb_model.predict(transformed_input)
        probability = nb_model.predict_proba(transformed_input).max()

        # Display the prediction
        st.write(f"Predicted category: {prediction[0]}")
        st.write(f"Prediction confidence: {probability:.2f}")

if __name__ == "__main__":
    main()
