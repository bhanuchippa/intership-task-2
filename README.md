# Sentiment Analysis NLP Project

A professional, production-ready Natural Language Processing (NLP) project developed for customer review sentiment classification. This project uses **TF-IDF Vectorization** and **Logistic Regression** to predict whether a review is Positive or Negative.

## 🚀 Features
- **Real-time Prediction**: Instantly classify reviews as Positive or Negative.
- **NLP Pipeline**: Full preprocessing including lowercasing, stopword removal, and stemming.
- **Modern UI**: Premium glassmorphism design with responsive layout and smooth animations.
- **Model Insights**: Display model accuracy and confusion matrix visualization.
- **Lightweight**: Optimized for low-end laptops and fast execution.
- **Modular Structure**: Clean and organized codebase ready for GitHub.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **NLP**: NLTK
- **Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)

## 📂 Project Structure
```text
SentimentAnalysisProject/
│
├── app.py                  # Flask Web Server
├── model/
│   ├── train_model.py      # Training Script
│   ├── vectorizer.pkl      # Saved TF-IDF Vectorizer
│   ├── sentiment_model.pkl # Saved Logistic Regression Model
│   └── accuracy.txt        # Stored model accuracy
│
├── static/
│   ├── css/style.css       # Premium Styling
│   └── js/script.js        # Frontend Logic
│
├── templates/
│   └── index.html          # Main Web Page
│
├── outputs/
│   └── confusion_matrix.png # Model Evaluation Plot
│
├── dataset/
│   └── reviews.csv         # Training Data
│
├── requirements.txt        # Project Dependencies
├── README.md               # Project Documentation
└── QUICK_START.md          # Beginner's Guide
```

## 🧠 NLP Workflow
1. **Data Loading**: Load customer reviews from CSV.
2. **Text Preprocessing**:
   - Lowercasing
   - Removing special characters/numbers
   - Tokenization
   - Stopword Removal (using NLTK)
   - Stemming (Porter Stemmer)
3. **Vectorization**: Convert text to numerical form using TF-IDF (Term Frequency-Inverse Document Frequency).
4. **Model Training**: Train a Logistic Regression Classifier on the vectorized data.
5. **Evaluation**: Generate accuracy scores and confusion matrices.

## 💻 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SentimentAnalysisProject.git
   cd SentimentAnalysisProject
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```
4. **Access the App**: Open `http://127.0.0.1:5000` in your browser.

## 📊 Expected Outputs
- **Sentiment Prediction**: Positive or Negative label with confidence percentage.
- **Accuracy**: Based on the training data (displayed on the dashboard).
- **Confusion Matrix**: Visual representation of model performance.

## 🔮 Future Improvements
- Add support for Neutral sentiment.
- Integrate Deep Learning models (LSTM/BERT).
- Implement real-time data scraping for reviews.
- Multi-language support.

---
*Created for Internship Task - 2024*
