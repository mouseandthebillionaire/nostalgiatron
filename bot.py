#!/usr/bin/python

from secrets import *

import random
import tweepy

# twitter setup
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

#get noises
noiseText = open('noises.txt')
noiseList = noiseText.readlines()

#get intro text
introText = open('intro.txt')
introList = introText.readlines()
introNum = random.randrange(len(introList))
intro = introList[introNum]

#get item
itemText = open('items.txt')
itemList = itemText.readlines()
itemNum = random.randrange(len(itemList))
item = itemList[itemNum]

n1chance = random.randrange(0, 5)
if n1chance > 1:
	n1 = noiseList[random.randrange(len(noiseList))]
else:
	n1 = ''
	
n2chance = random.randrange(0, 5)
if n2chance > 2:
	n2 = noiseList[random.randrange(len(noiseList))]
else:
	n2 = ''	
	
n3chance = random.randrange(0, 5)
if n3chance > 3:
	n3 = noiseList[random.randrange(len(noiseList))]
else:
	n3 = ''	

		
tweet = n1 + intro + n2 + item + n3
tweet = tweet.replace('\n', '')

print tweet
api.update_status(tweet)

