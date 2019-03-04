"""
The bot TWEET lines from Harry Potter and the Sorcerer's Stone book located within a text file called hp_books.txt
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

# Open the hp1.txt file 
my_file = open('hp_book1.txt', 'r')

# Read lines one by one from hp1.txt and assign file_lines variable 
file_lines = my_file.readlines()

# Close the hp1.txt file 
my_file.close()

# Define code blocks as functions and add additional sleep() functions to handle different situations 
def tweet():
	# Create a for loop to interate over file_lines 
	for line in file_lines:
		# Add try...except block to catch and output errors 
		try:
			print(line)
			# Add if statement to ensure that blank lines are skipped
			if line != '\n':
				# This function is used to update the status 
				api.update_status(line)
				# Add 5leep function to automate when the status will update (every minute in this case)
				sleep(5)
			# Add an else statement with pass to conclude the conditional statement 
			else:
				pass
		except tweepy.TweepError as e:
			print(e.reason)
			# Add sleep method to provide error messages and then repeat the loop after 5 seconds 
			sleep(5)
tweet()
