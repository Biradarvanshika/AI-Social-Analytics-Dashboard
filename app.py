# app.py
# To run this:
# 1. Install necessary libraries: pip install "transformers[torch]" safetensors Flask Flask-Cors tweepy praw
# 2. Get your API keys from Twitter/X and Reddit developer portals.
# 3. Fill in the placeholders below with your keys.
# 4. Run the script from your terminal: python app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import re
from collections import Counter
import tweepy
import praw

# --- Initialization ---
app = Flask(__name__)
CORS(app)

# --- API Keys (IMPORTANT: Replace with your own keys) ---
# It's best practice to use environment variables for these in a real project
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGlt3AEAAAAAZSCnpBAW1wnmUBbE1Qm0mC%2BKTTQ%3DEyp4C9dnQmspnUCHv7P8syU0DGX6wpBcE4EguSRzUni4KCIm77"
REDDIT_CLIENT_ID = "-zb2tKdKusQW49EDQ6fvug"
REDDIT_CLIENT_SECRET = "KqHPw7HxdS0qMvV-YjCAXGl9ZUcpYQ"
REDDIT_USER_AGENT = "SocialSentimentDashboard by u/YourUsername"

# --- Load AI Models ---
print("Loading AI models... This might take a moment.")
try:
    # *** THE FIX IS HERE ***
    # We add truncation=True to tell the pipeline to automatically handle long text.
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", truncation=True)
    emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", truncation=True)
    print("AI models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")
    sentiment_pipeline = None
    emotion_pipeline = None

# --- Live Data Fetching ---
def fetch_live_posts(topic, max_results=30):
    """Fetches and combines posts from Twitter and Reddit."""
    posts = []
    
    # Fetch from Twitter/X
    try:
        if TWITTER_BEARER_TOKEN != "YOUR_TWITTER_BEARER_TOKEN_HERE":
            twitter_client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
            query = f"{topic} -is:retweet lang:en"
            response = twitter_client.search_recent_tweets(query=query, max_results=max_results // 2, tweet_fields=["text", "author_id"])
            if response.data:
                for tweet in response.data:
                    # To get a username, you'd need to make another API call. For simplicity, we use author_id.
                    posts.append({"user": f"User {tweet.author_id} (Twitter)", "text": tweet.text})
    except Exception as e:
        print(f"Could not fetch from Twitter: {e}")

    # Fetch from Reddit
    try:
        if REDDIT_CLIENT_ID != "YOUR_REDDIT_CLIENT_ID_HERE":
            reddit = praw.Reddit(
                client_id=REDDIT_CLIENT_ID,
                client_secret=REDDIT_CLIENT_SECRET,
                user_agent=REDDIT_USER_AGENT,
            )
            subreddit = reddit.subreddit("all")
            for submission in subreddit.search(topic, limit=max_results // 2):
                text_content = submission.title
                if submission.selftext:
                    text_content += ". " + submission.selftext
                posts.append({"user": f"u/{submission.author} (Reddit)", "text": text_content})
    except Exception as e:
        print(f"Could not fetch from Reddit: {e}")
        
    # Fallback to mock data if both APIs fail or return nothing
    return posts if posts else fetch_mock_posts(topic)

# --- Mock Data (as a fallback) ---
def fetch_mock_posts(topic):
    sample_posts = {
        "labubu": [{"user": "@collector_jane", "text": "Just got the new Labubu figure! The quality is incredible. #labubu"}],
        "default": [{"user": "@techGuru", "text": "The new #SuperPhone is amazing! Battery life is insane."}]
    }
    return sample_posts.get(topic.lower(), sample_posts["default"])

# --- Helper Functions ---
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# --- API Endpoints ---
@app.route('/api/analyze', methods=['GET'])
def analyze_topic():
    if not sentiment_pipeline or not emotion_pipeline:
        return jsonify({"error": "AI models are not available."}), 500

    topic = request.args.get('topic')
    if not topic:
        return jsonify({"error": "Topic parameter is required."}), 400

    posts = fetch_live_posts(topic)

    sentiments = Counter()
    emotions = Counter()
    all_keywords = []
    analyzed_feed = []

    for post in posts:
        clean = clean_text(post['text'])
        if not clean: continue

        try:
            sentiment_result = sentiment_pipeline(clean)[0]
            sentiment_label = sentiment_result['label'].lower()
            sentiments[sentiment_label] += 1
            
            emotion_results = emotion_pipeline(clean)[0]
            top_emotion = max(emotion_results, key=lambda x: x['score'])
            emotions[top_emotion['label']] += 1

            analyzed_feed.append({"user": post['user'], "text": post['text'], "sentiment": sentiment_label})

            words = re.findall(r'#?\w+', post['text'].lower())
            all_keywords.extend([w for w in words if len(w) > 3 and w != topic.lower()])
        except Exception as e:
            print(f"Could not analyze post: {post['text'][:50]}... | Error: {e}")


    top_keywords = [kw for kw, count in Counter(all_keywords).most_common(10)]
    
    response_data = {
        "sentiment": {
            "positive": sentiments.get('positive', 0) + sentiments.get('optimism', 0),
            "negative": sentiments.get('negative', 0) + sentiments.get('pessimism', 0),
            "neutral": sentiments.get('neutral', 0)
        },
        "emotions": dict(emotions),
        "feed": analyzed_feed,
        "keywords": top_keywords
    }
    return jsonify(response_data)

@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    message = data.get('message', '').lower()
    response = "I'm a simple AI for now. Ask me about positive or negative keywords."
    if "complaint" in message or "negative" in message:
        response = "Based on the data, negative feedback often mentions 'price' and 'availability'."
    elif "like" in message or "positive" in message:
        response = "People seem to love the 'design' and 'new features'."
    return jsonify({"response": response})

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)

