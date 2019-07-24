from credentials import * 
import tweepy 
from time import sleep 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print('this is @techmariah (Mariah Rucker) twitter bot')

def retweet_favorite():
	for tweet in tweepy.Cursor(api.search, 
                             q="#HarryPotter", 
                             since='2019-02-25', 
                             until='2019-03-03', 
                             geocode='40.44496,-95.05640,100km', 
                             lang='en').items(15):
		try: 
			print('\nTweet by: @' + tweet.user.screen_name)
			tweet.retweet()
			
			print('#TeamGryffindor bot RETWEETED the tweet')
			tweet.favorite()
			
			print('#TeamGryffindor bot FAVORITED the tweet')
			if not tweet.user.following:
				tweet.user.follow()
				print('#TeamGryffindor bot FOLLOWED the user')
				
			sleep(2)
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break 
retweet_favorite()
