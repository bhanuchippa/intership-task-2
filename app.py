from flask import Flask, render_template, request, jsonify
import joblib
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK data (if not already downloaded)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)

# Paths
MODEL_PATH = os.path.join('model', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join('model', 'vectorizer.pkl')
ACCURACY_PATH = os.path.join('model', 'accuracy.txt')

# Load model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Load accuracy
accuracy = "0.0"
if os.path.exists(ACCURACY_PATH):
    with open(ACCURACY_PATH, 'r') as f:
        accuracy = f.read()

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

@app.route('/')
def home():
    return render_template('index.html', accuracy=accuracy)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        review = data.get('review', '')
        
        if not review:
            return jsonify({'error': 'No review provided'}), 400
        
        # Preprocess
        processed_review = preprocess_text(review)
        
        # Vectorize
        vectorized_review = vectorizer.transform([processed_review])
        
        # Predict
        prediction = model.predict(vectorized_review)[0]
        
        # Get probability (optional, but good for UI)
        probabilities = model.predict_proba(vectorized_review)[0]
        confidence = max(probabilities) * 100
        
        return jsonify({
            'sentiment': prediction,
            'confidence': round(confidence, 2),
            'processed_text': processed_review
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # Forced reload to load the 92% accuracy model.

