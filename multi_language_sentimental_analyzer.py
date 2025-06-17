# 💬 Multi-language Sentiment Analyzer by Amal M
# Analyze sentiment in Malayalam, Hindi, English, and more!

import streamlit as st
from transformers import pipeline
from googletrans import Translator
from datetime import datetime

# Initialize translator and sentiment model
translator = Translator()
sentiment_pipeline = pipeline("sentiment-analysis")

# Page config
st.set_page_config(page_title="Sentiment Analyzer by Amal", page_icon="🧠")
st.title("🧠 Multi-language Sentiment Analyzer")
st.markdown("Developed with ❤ by *Amal M\n\nSupports **Malayalam, **Hindi, **English*, and more!")

# Text Input
text_input = st.text_area("📥 Enter your text here:", height=150)

# Analyze Button
if st.button("🔍 Analyze Sentiment"):
    if not text_input.strip():
        st.warning("⚠ Please enter some text.")
    else:
        try:
            # Step 1: Translate input to English
            translation = translator.translate(text_input, dest='en')
            translated_text = translation.text

            # Step 2: Run sentiment analysis
            result = sentiment_pipeline(translated_text)[0]
            label = result['label']
            confidence = round(result['score'] * 100, 2)

            # Step 3: Display Results
            st.success("✅ Sentiment Analyzed Successfully")
            st.markdown(f"🗣 Original Text:** {text_input}")
            st.markdown(f"🌐 Translated (English):** {translated_text}")
            st.markdown(f"💬 Sentiment:** {label}")
            st.markdown(f"📊 Confidence Score:** {confidence}%")

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")