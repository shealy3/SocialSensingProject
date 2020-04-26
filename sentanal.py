import re
import sys
import tweepy
import json
from tweepy import OAuthHandler
from textblob import TextBlob


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(parsed_tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(parsed_tweet['text']))
    # set sentiment
    parsed_tweet['sentnum'] = analysis.sentiment.polarity
    if analysis.sentiment.polarity > 0.5:
        parsed_tweet['sentiment'] = 'positive'
    elif analysis.sentiment.polarity < 0:
        parsed_tweet['sentiment'] = 'negative'
    else:
        parsed_tweet['sentiment'] = 'neutral'
    return parsed_tweet


def get_tweets(tweetlist):
    '''
    Main function to fetch tweets and parse them.
    '''
    # empty list to store parsed tweets
    tweets = []
    # parsing tweets one by one
    for tweet in tweetlist:
        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        parsed_tweet["id"] = tweet.id
        # saving text of tweet
        parsed_tweet["text"] = tweet.text
        # saving sentiment of tweet
        parsed_tweet = get_tweet_sentiment(parsed_tweet)

        # appending parsed tweet to tweets list
        if tweet.retweets > 0:
            # if tweet has retweets, ensure that it is appended only once
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        else:
            tweets.append(parsed_tweet)

    # return parsed tweets
    return tweets


def analyze_tweets(tweetlist):
    # get input file name from command line
    #infile = sys.argv[1]

    # load in tweets from input file
    #tweetlist = []
    #f = open(infile, "r")
    #for x in f:
    #    tweetlist.append(json.loads(x))
    #f.close()
    tweets = get_tweets(tweetlist=tweetlist)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # percentage of positive tweets
    '''print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))

    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))'''

    sumtweet = 0
    #print("Score")
    for tweet in tweets:
        sumtweet = sumtweet + tweet['sentnum']
    #print("Sum of scores:")
    #print(sumtweet)
    return sumtweet


def analyze_tweets_print(tweetlist, base):
    # get input file name from command line
    #infile = sys.argv[1]

    # load in tweets from input file
    #tweetlist = []
    #f = open(infile, "r")
    #for x in f:
    #    tweetlist.append(json.loads(x))
    #f.close()
    tweets = get_tweets(tweetlist=tweetlist)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))

    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    sumtweet = 0
    print("Score")
    for tweet in tweets:
        sumtweet = sumtweet + tweet['sentnum']
    print("Sum of scores:")
    print(sumtweet-base)
