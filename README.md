AI Social Media Analytics Dashboard

A full-stack web application that performs real-time sentiment and emotion analysis on social media posts for any given topic. Built with a Python/Flask backend and a dynamic, responsive frontend.

✨ Features
Real-time Sentiment Analysis: Classifies posts as Positive, Negative, or Neutral.

Emotion Detection: Identifies emotions like Joy, Anger, Sadness, etc.

Live Data Feed: Fetches and displays posts from Twitter/X and Reddit.

Key Topic Extraction: Shows a word cloud of the most common keywords.

Conversational AI Analyst: A chatbot to ask questions about the analyzed data.

Custom UI: A dynamic, animated "Synthwave" theme with a custom cursor.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript, TailwindCSS, Chart.js

NLP: Hugging Face Transformers (RoBERTa models)

Data Fetching: Tweepy (for Twitter/X), PRAW (for Reddit)

🚀 How to Run
Clone the repository:

git clone https://github.com/Biradarvanshika/AI-Social-Analytics-Dashboard.git
cd AI-Social-Analytics-Dashboard

Install the required libraries:

pip install -r requirements.txt

Add your API Keys:

Open the app.py file.

Add your own secret keys for TWITTER_BEARER_TOKEN, REDDIT_CLIENT_ID, and REDDIT_CLIENT_SECRET.

Run the backend server:

python app.py

The server will start on http://127.0.0.1:5000.

Open the frontend:

Open the dashboard.html file in your web browser.

