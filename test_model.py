import joblib
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Setup
model = joblib.load('model/sentiment_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

def preprocess_text(text):
    if not isinstance(text, str): return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

test_reviews = ["very bad product", "I love it", "worst experience", "excellent quality", "bad product", "good product"]

for review in test_reviews:
    proc = preprocess_text(review)
    vec = vectorizer.transform([proc])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    print(f"Review: '{review}' -> Processed: '{proc}' -> Prediction: {pred} ({max(prob)*100:.2f}%)")
