# libiraries
import numpy as np
import pandas as pd
import re
import streamlit as st

from keras.preprocessing.sequence import pad_sequences

# Load the model and tokenizer
# %%
import pickle
with open('model_tokenizer.pkl', 'rb') as file:
    model, tokenizer= pickle.load(file)
# %%
def clean_text(text):
    text = text.lower()
    text = re.sub(r'(#|@)\w*', '', text)  # Remove hashtags and mentions
    text = re.sub("https?:\/\/\S+", '', text)  # Remove links
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text
# Preprocess the text function
def preprocess_text(text, tokenizer):
    text = clean_text(text)
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=100)  # Adjust maxlen based on your model's input shape
    return padded

# Streamlit App
st.title('Tweet Sentiment Analyzer')

# Input for Tweet
tweet = st.text_input('Enter a Tweet:')

# Analyze Tweet
if st.button('Analyze'):
    processed_tweet = preprocess_text(tweet, tokenizer)
    prediction = model.predict(processed_tweet)
    sentiment = 'Positive' if prediction[0][1] >= 0.5 else 'Negative'
    st.write(f"Predicted Sentiment: {sentiment}")
