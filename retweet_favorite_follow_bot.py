"""
The bot RETWEET, FAVORITE and FOLLOW users who mentions the key hashtag #HarryPotter 
"""

# Import our Twitter credentials from credentials.py 
from credentials import * 
# Import tweepy library to interact wihth the Twitter API
import tweepy 
# Import sleep function from time module to automate tweet status submissions 
from time import sleep 

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print('this is @techmariah (Mariah Rucker) twitter bot')

def retweet_favorite():
	# For loop to iterate over tweets with #HarryPotter, limit to 15 
	for tweet in tweepy.Cursor(api.search, 
                             q="#HarryPotter", 
                             since='2019-02-25', 
                             until='2019-03-03', 
                             geocode='40.44496,-95.05640,100km', 
                             lang='en').items(15):

		# Add error handling "try...except" and StopIteration exception to break the loop
		try: 
			# Print out the usernames of the last 10 people to use the #HarryPotter hashtag 
			# Add \n escape character to print() to organize tweets 
			print('\nTweet by: @' + tweet.user.screen_name)

			# RETWEET tweets as they are found, print out "Retweet the tweet" and loop again after 5 seconds 
			tweet.retweet()
			print('#TeamGryffindor bot RETWEETED the tweet')

			# FAVORITE the tweet
			tweet.favorite()
			print('#TeamGryffindor bot FAVORITED the tweet')

			# FOLLOW the user who tweeted 
			if not tweet.user.following:
				tweet.user.follow()
				print('#TeamGryffindor bot FOLLOWED the user')

			sleep(2)
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break 
retweet_favorite()
