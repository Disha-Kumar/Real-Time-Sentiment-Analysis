import numpy as np

def analyze_sentiment(tweet, model, vectorizer, lb):
    X_tweet = vectorizer.transform([tweet])
    prediction = model.predict(X_tweet.toarray())
    predicted_sentiment = lb.inverse_transform(prediction)[0]
    return predicted_sentiment
