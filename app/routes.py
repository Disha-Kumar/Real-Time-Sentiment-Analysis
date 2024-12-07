from flask import Flask, jsonify, request, render_template
from data.collect_data import collect_data
from data.process_data import process_data
from ml.train_model import train_model
from app.models import analyze_sentiment
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    data = request.json
    tweet = data['tweet']
    
    df = collect_data(api_key, api_secret_key, access_token, access_token_secret, query)
    X, vectorizer = process_data(df)
    y = df['sentiment']  # Assuming sentiment labels are available
    model, lb = train_model(X, y)
    sentiment = analyze_sentiment(tweet, model, vectorizer, lb)
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
