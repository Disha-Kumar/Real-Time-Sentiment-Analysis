import tweepy
import pandas as pd

def collect_data(api_key, api_secret_key, access_token, access_token_secret, query, count=100):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = api.search(q=query, count=count, lang='en', tweet_mode='extended')
    data = [{'tweet': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
    df = pd.DataFrame(data)
    return df

# Example usage
api_key = 'your_api_key'
api_secret_key = 'your_api_secret_key'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
query = 'your_brand_or_product'
df = collect_data(api_key, api_secret_key, access_token, access_token_secret, query)
print(df)
