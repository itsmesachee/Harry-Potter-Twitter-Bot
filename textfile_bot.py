from credentials import * 
import tweepy 
from time import sleep 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print('this is @techmariah (Mariah Rucker) twitter bot')

my_file = open('hp_book1.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

def tweet():
	for line in file_lines:
		try:
			print(line)
			if line != '\n':
				api.update_status(line)
				sleep(5)
			else:
				pass
		except tweepy.TweepError as e:
			print(e.reason)
			sleep(5)
tweet()
