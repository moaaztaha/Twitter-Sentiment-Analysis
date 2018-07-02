print("Collecting Data....")
from textblob import TextBlob 
import tweepy 

consumer_key = 'Consumer Key'
consumer_secret = 'Consumer Secret'

access_token = 'Access Token'
access_token_secret = 'Access Token Secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


tweets  = api.user_timeline("sirajraval", count = 100)

polarity = 0
subjectivity = 0



for tweet in tweets:
	analysis = TextBlob(tweet.text)
	polarity += analysis.sentiment.polarity
	subjectivity += analysis.sentiment.subjectivity

print("Plarity and subjectivity per 100 Tweets:")
print("Polarity:",polarity)
print("Subjectivity:",subjectivity)