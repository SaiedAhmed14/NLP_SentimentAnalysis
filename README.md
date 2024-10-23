# NLP_SentimentAnalysis
Tweet Sentiment Analysis (Classify Tweets into positive &amp; Negative )

Over the past few hours , I’ve been working on developing a NLP model that analyzes the sentiment of tweets. From building the model to integrating it into a Streamlit app, it’s been an incredible journey. Here’s a quick breakdown of what we’ve accomplished:

🔍 Project Overview:
Objective: Analyze tweet sentiments (positive/negative) using machine learning.
Tools Used: Python, Pandas, Keras, Streamlit, Pickle.

🛠️ Steps:
Data Collection & Preprocessing:
Collected tweet data.
Cleaned text by removing hashtags, mentions, links, and special characters.
Model Development:
Tokenized the text using Keras Tokenizer.
Built a Sequential model with a Dense layer using Keras.
Trained the model on preprocessed tweet data.
Saving & Loading Models:
Saved the trained model and tokenizer using Pickle.
Loaded them into a Streamlit app for real-time predictions.
Streamlit App Development:
Created an interactive web app for users to input tweets and get sentiment analysis.
Displayed confidence scores for predictions.
