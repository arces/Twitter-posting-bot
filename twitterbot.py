#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

#end parseIn()



def newTweet(placeholderNoun, placeholderVerb, placeholderAdj, prepend, append):
	#Takes templates, nouns, verbs, and adjectives, stitches them together, and add whatever you like on either end
	nounN = random.randint(0, nouns.__len__()) #picks a random noun
	verbN = random.randint(0, verbs.__len__()) #picks a random line number
	adjN  = random.randint(0, adjs.__len__())  #picks a random line number
	templateN = random.randint(0, templates.__len__()) #


	tweet = prepend
	tweet = re.sub('\s+',' ',tweet) #Removes whitespaces (\n, \r\n, \t, space, and others) and replaces with spaces only
	tweet = tweet + append
	return tweet




def runBot(tweetDelay):
    '''Tweets a newTweet() every tweetDelay minutes.'''
	#enter the corresponding information from your Twitter application:
	CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
	CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
	ACCESS_KEY = ''#keep the quotes, replace this with your access token
	ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	administrativeTweet = random.randint(0,9)
    while(True):
        print "tweeting normal tweet"
        text=newTweet()
        administrativeTweet = administrativeTweet+1
        print text
		time.sleep(20)#waits 20 secs to kill program if need be
		api.update_status(status=text)
		print " "
		print "tweeted"
		time.sleep(tweetDelay * 60) #Tweet every n minutes
