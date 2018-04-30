# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3046206272-EihDXs7EIsKubmMuNlEnBS68mU1Mu2YMYzjcqFg'
ACCESS_SECRET = '18zloBQfhAqSyqmRiumAxjF9dpI4mcFXAX3kvyJxWHWh2'
CONSUMER_KEY = 'LHVbOiZULd7Xr8YLoijyUwnsO'
CONSUMER_SECRET = 'MDbWT4CyAJzRu49WVP1D7W3ruQHg7jvaaeVxq3clVQyVGwHQ0q'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
series_name = "bojack horseman"
iterator = twitter_stream.statuses.filter(track=series_name, language="en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 100
temp_str = ""
for tweet in iterator:
    
    try:
        if not tweet['retweeted']:
            tweet_count -= 1

    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
            temp_str = tweet['text'].lower()
            if series_name in temp_str:
                print(temp_str + "\n")

    
    except KeyError:
        tweet_count -= 1
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 