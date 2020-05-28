import tweepy
import os

# API Key
consumer_key = os.environ['ConsumerKeyVar']
consumer_secret = os.environ['ConsumerSecretVar']
access_key = os.environ['AccessKeyVar']
access_secret = os.environ['AccessSecretVar']

# Tweepy Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

myReplyTweet = []
mentionInReplyTweet = []
noDeleteTweet = []
deleteTweet = []


def lambda_handler(event, context):
    # Get My Reply
    print("==========Get My Reply==========")
    for tweet in tweepy.Cursor(api.user_timeline,exclude_replies = False,include_rts = False).items(200):
        if "@" in tweet.text and tweet.favorite_count == 0 and tweet.retweet_count == 0:
            print(tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count)
            myReplyTweet.append(tweet.id)
    
    # Get in_reply_to_status_id in mentions
    print("==========Reply Tweet==========")
    for mentions in tweepy.Cursor(api.mentions_timeline).items(400):
        print(mentions.id,mentions.created_at,mentions.text.replace('\n',''))
        mentionInReplyTweet.append(mentions.in_reply_to_status_id)
    
    # Extraction Delete Tweet
    print("==========Extraction Delete tweet==========")
    for mntnrptw in mentionInReplyTweet:
        for myrptw in myReplyTweet:
            if mntnrptw == myrptw:
                deleteTweet.append(myrptw)
    preparateDeleteTweet = set(myReplyTweet) ^ set(deleteTweet)
    print(list(preparateDeleteTweet))
    
    # Delete Tweet
    print("==========delete tweet==========")
    for deltw in preparateDeleteTweet:
        print(api.get_status(deltw).id,api.get_status(deltw).created_at,api.get_status(deltw).text)
        api.destroy_status(deltw)