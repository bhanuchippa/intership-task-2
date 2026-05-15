import pandas as pd
import numpy as np
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Download NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

def preprocess_text(text):
    # Ensure text is a string
    if not isinstance(text, str):
        return ""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenization
    tokens = nltk.word_tokenize(text)
    # Stopword removal
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    # Join tokens back to string
    return ' '.join(tokens)

def train():
    print("Starting Model Training...")
    
    # Paths
    dataset_path = os.path.join('dataset', 'reviews.csv')
    model_dir = 'model'
    output_dir = os.path.join('static', 'images')
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load dataset
    df = pd.read_csv(dataset_path)
    print(f"Dataset loaded with {len(df)} records.")

    # Preprocessing
    print("Preprocessing text data...")
    df['processed_review'] = df['review'].apply(preprocess_text)

    # Split data
    X = df['processed_review']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TF-IDF Vectorization
    print("Applying TF-IDF Vectorization...")
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train Logistic Regression
    print("Training Logistic Regression Model...")
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train_tfidf, y_train)

    # Predictions
    y_pred = model.predict(X_test_tfidf)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix Visualization
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(output_dir, 'confusion_matrix.png'))
    plt.close()
    print(f"Confusion matrix saved to {os.path.join(output_dir, 'confusion_matrix.png')}")

    # Save Model and Vectorizer
    joblib.dump(model, os.path.join(model_dir, 'sentiment_model.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))
    print("Model and Vectorizer saved successfully.")

    # Save accuracy to a file for the app to display
    with open(os.path.join(model_dir, 'accuracy.txt'), 'w') as f:
        f.write(str(round(accuracy * 100, 2)))

if __name__ == "__main__":
    train()
