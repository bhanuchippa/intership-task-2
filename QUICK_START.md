# 🚀 Quick Start Guide

Welcome to the Sentiment Analysis Project! Follow these simple steps to get the project running on your laptop in less than 2 minutes.

## 1. Prerequisites
Make sure you have Python installed. If not, download it from [python.org](https://www.python.org/).

## 2. Installation
Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
# Navigate to the project folder
cd SentimentAnalysisProject

# Install all required libraries
pip install -r requirements.txt
```

## 3. Run the App
To start the Flask web server, run:

```bash
python app.py
```

## 4. Open in Browser
Once the server starts, you will see a message like `Running on http://127.0.0.1:5000`.
Copy and paste this URL into your web browser:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## 🛠️ Troubleshooting
- **Error: "pip not recognized"**: Ensure Python is added to your system PATH during installation.
- **Error: "ModuleNotFoundError"**: Re-run `pip install -r requirements.txt`.
- **Port 5000 in use**: You can change the port in `app.py` by editing `app.run(port=5001)`.
- **NLTK Download Issues**: The app tries to download NLTK data automatically. If it fails, ensure you have an internet connection on first run.

## ✅ Success!
You should now see the modern Sentiment Analysis dashboard. Type any review and click "Analyze" to see the magic!
