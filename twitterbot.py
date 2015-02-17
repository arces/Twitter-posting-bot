#! /usr/bin/python
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret

OPTION_DELAY = 30 #Delay between tweets in minutes. You are allowed at most 2400 tweets/day or 100 tweets/hour, but the bot itself does not limit you.
OPTION_PLACEHOLDER_N = "_N_" #The placeholder for nouns in your templates
OPTION_PLACEHOLDER_V = "_V_" #The placeholder for verbs in your templates
OPTION_PLACEHOLDER_A = "_A_" #The placeholder for adjectives in your templates
OPTION_PREPEND = ""		  #This is added to the beginning of each tweet
OPTION_APPEND =  "#YOLO"	 #This is added to the end of each tweet.
OPTION_CENSOR_DELAY = 1	  #How long to wait, in seconds, after printing but befoe posting the tweet.

import tweepy, time, sys, random, json, re, datetime

random.seed() #Make sure our randoms are random

def parseIn():
	i = 0
	nouns = []
	f = open('nouns.txt', 'r')
	line = f.readline() #Read a line from the file
	while (line != ''):
		#line = re.sub('\s+','',line)
		nouns.append(line)			 #Store the word
		i = i + 1
		line = f.readline() #Read a new line



	i = 0
	verbs = []
	f = open('verbs.txt', 'r')
	line = f.readline() #Read a line from the file
	while (line != ''):
		#line = re.sub('\s+','',line)
		verbs.append(line)			 #Store the word
		i = i + 1
		line = f.readline() #Read a new line



	i = 0
	adjs = []
	f = open('adjectives.txt', 'r')
	line = f.readline() #Read a line from the file
	while (line != ''):
		#line = re.sub('\s+','',line)
		adjs.append(line)			 #Store the word
		i = i + 1
		line = f.readline() #Read a new line


	i = 0
	templates = []
	f = open('templates.txt', 'r')
	line = f.readline() #Read a line from the file
	while (line != ''):
		templates.append(line)			 #Store the word
		i = i + 1
		line = f.readline() #Read a new line
	i = 0
	return nouns, verbs, adjs, templates
#end parseIn()



def newTweet(placeholderNoun, placeholderVerb, placeholderAdj, prepend, append):
	#Takes templates, nouns, verbs, and adjectives, stitches them together, and add whatever you like on either end
	nounN = random.randint(0, nouns.__len__() - 1) #picks a random noun
	verbN = random.randint(0, verbs.__len__() - 1) #picks a random verb
	adjN  = random.randint(0, adjs.__len__() - 1)  #picks a random adjective
	templateN = random.randint(0, templates.__len__() - 1) #picks a random template
	tweet = prepend
	tweet = templates[templateN]
	tweet = re.sub(placeholderNoun, nouns[nounN], tweet) #Replace noun placeholder with a noun
	tweet = re.sub(placeholderVerb, verbs[verbN], tweet) #Replace verb placeholder with a verb
	tweet = re.sub(placeholderAdj, adjs[adjN], tweet) #Replace adjective placeholder with an adjective
	tweet = re.sub('\s+',' ',tweet) #Removes whitespaces (\n, \r\n, \t, space, and others) and replaces with spaces only
	tweet = tweet + append
	return tweet

#end newTweet()




def runBot():
	'''Tweets a newTweet() every OPTION_DELAY minutes.'''
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	while(True):
		print "Generating...\n"
		text=newTweet(OPTION_PLACEHOLDER_N, OPTION_PLACEHOLDER_V, OPTION_PLACEHOLDER_A, OPTION_PREPEND, OPTION_APPEND)
		print text
		print "\n" + str(OPTION_CENSOR_DELAY) + " seconds to cancel tweet..."
		time.sleep(OPTION_CENSOR_DELAY)#waits so the user can kill the program if need be
		print "Tweeting..."
		api.update_status(status=text)
		print "Tweeted! Next tweet in " + str(OPTION_DELAY) + " minutes."
		time.sleep(OPTION_DELAY * 60) #Tweet every n minutes
#end runBot()


nouns, verbs, adjs, templates = parseIn()
runBot()
