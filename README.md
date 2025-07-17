# 🎯 AI Social Media Analytics Dashboard

A full-stack web application that performs **real-time sentiment and emotion analysis** on social media posts for any given topic.  
Built with a Python/Flask backend and a dynamic, responsive **"Synthwave" themed UI**.

![Dashboard Demo](https://github.com/Biradarvanshika/AI-Social-Analytics-Dashboard/assets/175276903/b7c41f90-1996-419b-8e27-02059367358d)

---

## ✨ About The Project

In today's fast-paced digital world, public opinion can shift in an instant.  
This tool was built to provide a **live, at-a-glance understanding of the public conversation** around any topic.

By fetching data directly from **Twitter/X** and **Reddit**, it uses **Natural Language Processing** to analyze not just whether the sentiment is positive or negative, but also the **specific emotions** driving the conversation.

This project showcases a complete **full-stack development cycle**, from backend data processing and AI modeling to a polished, interactive frontend user experience.

---

## 🛠️ Built With

| Technology              | Description                                                   |
|-------------------------|---------------------------------------------------------------|
| `Python`                | The core language for the backend and AI logic.               |
| `Flask`                 | A lightweight web framework for serving the API.              |
| `Hugging Face Transformers` | State-of-the-art library for NLP models (Sentiment & Emotion). |
| `Tweepy` & `PRAW`       | Libraries for fetching live data from Twitter/X and Reddit.   |
| `HTML`, `CSS`, `JavaScript` | The foundation of the user interface.                   |
| `TailwindCSS`           | A utility-first CSS framework for rapid UI development.       |
| `Chart.js`              | For creating beautiful, interactive charts and graphs.        |

---

## 🚀 How to Run

1. Clone the repository
```bash
git clone https://github.com/Biradarvanshika/AI-Social-Analytics-Dashboard.git
cd AI-Social-Analytics-Dashboard
 2. Install the required libraries
bash
Copy
Edit
pip install -r requirements.txt
3. Add your API Keys
Open the app.py file.

Add your secret keys for:

TWITTER_BEARER_TOKEN

REDDIT_CLIENT_ID

REDDIT_CLIENT_SECRET

4. Run the backend server
bash
Copy
Edit
python app.py
The server will start at: http://127.0.0.1:5000

5. Open the frontend
Open the dashboard.html file in your web browser.

📌 Features
Real-time sentiment & emotion analysis

Pulls live data from Twitter and Reddit

Interactive charts and responsive design

Synthwave-themed UI for modern feel

📬 Contact
Have questions or suggestions?
Feel free to reach out via GitHub Issues.

