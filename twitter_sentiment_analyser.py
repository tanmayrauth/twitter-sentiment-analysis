import tweepy
import pandas as pd
from textblob import TextBlob


#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

tweet_list = []
sentiment_list = []
public_tweets = api.search("awesome")
for tweet in public_tweets:
    tweet_list.append( ascii(tweet.text) )
    analyser = TextBlob(ascii(tweet.text))
    pol = analyser.sentiment.polarity
    print(pol)
    if(pol > 0):
        sentiment_list.append("Positive")
    else:
        sentiment_list.append("Negative")

dataFrame = pd.DataFrame({'Tweet':tweet_list, 'Sentiment':sentiment_list})
print(dataFrame)
dataFrame.to_csv('sentiment_result.csv', sep = '\t', encoding = 'utf-8')
