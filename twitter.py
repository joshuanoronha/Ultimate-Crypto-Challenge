from texttable import Texttable
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'ug31mn60un6McZcvoXZ63P3Eo'
        consumer_secret = '0fRdInGabqTFPYqjaLpMTCtkzFwCwc5QtCbz5T1akcVNqQn1JC'
        access_token = '842999900778455041-dBplFFiIC6j4n6qfM5gqqI5mEtQONj5'
        access_token_secret = 'IOfYQiWzviKeFTeqoI4fdxHjm37CtpBbZsOCEcXDU7eRc'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets

            fetched_tweets = []

            for i in range(1):
                fetched_tweets.extend( self.api.search(q=query, rpp=count, count=100 ))

            print (len(fetched_tweets))
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                parsed_tweet['followers_count'] = tweet.user.followers_count
                parsed_tweet['retweet_count'] = tweet.retweet_count
                parsed_tweet['favorite_count'] = tweet.favorite_count
                parsed_tweet['id'] = tweet.id
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                parsed_tweet['time'] = tweet.created_at
                # saving sentiment of tweet
                # import code; code.interact(local=locals())

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)


                # print (dir(tweet))
                # import code; code.interact(local=locals())
                # import sys
                # sys.exit(0)
                #



            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    print("Testing")
    tweets = api.get_tweets(query = 'bitcoin', count = 100)
    #
    # # picking positive tweets from tweets
    # ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # # percentage of positive tweets
    # print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # # picking negative tweets from tweets
    # ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # # percentage of negative tweets
    # print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # # percentage of neutral tweets
    # #print("Neutral tweets percentage: {} %".format(100*len(tweets - ntweets - ptweets)/len(tweets)))
    #
    # # printing first 5 positive tweets
    # print("\n\nPositive tweets:")
    # for tweet in ptweets[:10]:
    #     print(tweet['text'])
    #
    # # printing first 5 negative tweets
    # print("\n\nNegative tweets:")
    # for tweet in ntweets[:10]:
    #     print(tweet['text'])

    t = Texttable()
    t.add_row(["fol.","re","fav","sentiment", "text", "time"])
    for h in tweets:
        #

        t.add_row([h['followers_count'], h['retweet_count'], h['favorite_count'], h['sentiment'], h['text'], str(h['time'])])
    print( t.draw())
    print(len(tweets))
    
    mfile = open("twitter.csv", "w")
    mfile.write(", ".join(["fol.","re","fav","sentiment", "text", "time"])+ "\n") 
    for h in tweets:
        mfile.write(", ".join(map(lambda x: str(x).replace(",", ";").replace("\n", " "),[h['followers_count'],
                             h['retweet_count'],
                             h['favorite_count'],
                             h['sentiment'],  
                             h['text'], 
                             str(h['time'])]))+ "\n")

        
    
    

if __name__ == "__main__":
    # calling main function
    main()
