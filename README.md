📄 [Download the formatted PDF version of this README](./AI_Social_Analytics_Dashboard_README.pdf)



AI Social Media Analytics Dashboard
A full-stack web application that performs real-time sentiment and emotion analysis on social media posts for any given topic. Built with a Python/Flask backend and a dynamic, responsive "Synthwave" themed UI.

<br>

https://github.com/Biradarvanshika/AI-Social-Analytics-Dashboard/assets/175276903/b7c41f90-1996-419b-8e27-02059367358d

✨ About The Project
In today's fast-paced digital world, public opinion can shift in an instant. This tool was built to provide a live, at-a-glance understanding of the public conversation around any topic. By fetching data directly from social media platforms like Twitter/X and Reddit, it uses Natural Language Processing to analyze not just whether the sentiment is positive or negative, but also the specific emotions driving the conversation.

This project showcases a complete full-stack development cycle, from backend data processing and AI modeling to a polished, interactive frontend user experience.

🛠️ Built With
This project was brought to life with these modern technologies:

Tech

Description

Python

The core language for the backend and AI logic.

Flask

A lightweight web framework for serving the API.

Hugging Face Transformers

State-of-the-art library for NLP models (Sentiment & Emotion).

Tweepy & PRAW

Libraries for fetching live data from Twitter/X and Reddit.

HTML, CSS, JavaScript

The foundation of the user interface.

TailwindCSS

A utility-first CSS framework for rapid UI development.

Chart.js

For creating beautiful, interactive charts and graphs.

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
