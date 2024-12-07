import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def process_data(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['tweet'])
    return X, vectorizer

# Example usage
df = collect_data(api_key, api_secret_key, access_token, access_token_secret, query)
X, vectorizer = process_data(df)
print(X.shape)
