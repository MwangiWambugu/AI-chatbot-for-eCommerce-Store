import pandas as pd
from joblib import load
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Assuming you have downloaded these datasets previously
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

def preprocess_question(question):
    """
    Preprocesses the input question by lowercasing, tokenizing, removing stopwords, and lemmatizing.
    """
    # Convert to lowercase
    question = question.lower()
    # Tokenize
    tokens = word_tokenize(question)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    # Join back into a string
    preprocessed_question = ' '.join(lemmatized_tokens)
    return preprocessed_question

def predict_intent(question, vectorizer, model):
    """
    Predicts the intent of the given question using the loaded vectorizer and model.
    """
    # Preprocess the question
    preprocessed_question = preprocess_question(question)
    # Vectorize the question
    question_vect = vectorizer.transform([preprocessed_question])
    # Predict the intent
    predicted_intent = model.predict(question_vect)[0]
    return predicted_intent

def get_response(intent):
    """
    Returns a natural language response based on the predicted intent.
    """
    # Example response mapping
    response_mapping = {
        'Product Authenticity': "To verify product authenticity, please check the product's unique identification code on our official website.",
        'Health and Safety': "For health and safety information, refer to the product's safety guidelines or contact our support team.",
        # Add more mappings based on your intents
    }
    return response_mapping.get(intent, "Sorry, I'm not sure how to respond to that.")

def main():
    # Load the saved model and vectorizer
    model = load('nb_model.joblib')
    vectorizer = load('tfidf_vectorizer.joblib')

    # Input question
    question = input("Please enter your question: ")

    # Predict the intent
    intent = predict_intent(question, vectorizer, model)
    
    # Generate a response
    response = get_response(intent)
    
    print("Response:", response)

if __name__ == "__main__":
    main()
