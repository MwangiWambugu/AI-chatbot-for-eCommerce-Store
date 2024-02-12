import random
from joblib import load
from nltk.stem import WordNetLemmatizer  
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords

# Load model, vectorizer, label encoder
model = load('nb_model.joblib')
vectorizer = load('tfidf_vectorizer.joblib')
le = load('label_encoder.joblib')

# Initialize lemmatizer 
lemmatizer = WordNetLemmatizer()

# Sample usernames
usernames = ['Mary', 'John', 'Sarah']

# Potential responses 
responses = [
  "Hi {name}, based on your question, I think you're asking about {intent} of this product. Let me know if I can help explain that!",  
  "Great question, {name}! It looks like you are interested in knowing more about the {intent}. I'm happy to share more details."   
]

# User interaction loop
while True:

  # Get user details
  username = random.choice(usernames)
  user_question = input("What is your question?")
  
  # Preprocess user question
  tokens = word_tokenize(user_question)
  lower_tokens = [t.lower() for t in tokens]
  no_punct_tokens = [t for t in lower_tokens if t.isalpha()]
  
  # Lemmatize
  lemmatized_tokens = [lemmatizer.lemmatize(t) for t in no_punct_tokens] 
  
  # Remove stopwords
  no_stop_tokens = [t for t in lemmatized_tokens if not t in stopwords.words('english')]

  # Join back into string
  preprocessed_question = " ".join(no_stop_tokens)
  
  # Vectorize 
  vect_question = vectorizer.transform([preprocessed_question])

  # Prediction
  predicted_intent = model.predict(vect_question)[0]
  predicted_label = le.inverse_transform([predicted_intent])[0]

  # Construct response
  response = random.choice(responses).format(name=username, intent=predicted_label)

  # Display response
  print(response)
  
  # Check to continue
  choice = input("Continue conversation? (y/n)")
  if choice.lower() != 'y':
    break
