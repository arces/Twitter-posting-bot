#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random, json, re, datetime
 
random.seed()

i = 0
nouns = []
f = open('nouns.txt', 'r') 
line = f.readline() #Read a line from the file
while (line != ''):
	line = re.sub('\s+','',line)
	nouns.append(line)             #Store the word
	i = i + 1
	line = f.readline() #Read a new line

numnouns = i

i = 0
verbs = []
f = open('verbs.txt', 'r') 
line = f.readline() #Read a line from the file
while (line != ''):
	line = re.sub('\s+','',line)
	verbs.append(line)             #Store the word
	i = i + 1
	line = f.readline() #Read a new line

numverbs = i

i = 0
adjs = []
f = open('adjectives.txt', 'r') 
line = f.readline() #Read a line from the file
while (line != ''):
	line = re.sub('\s+','',line)
	adjs.append(line)             #Store the word
	i = i + 1
	line = f.readline() #Read a new line

numadjs = i


def newtweet(seqnum):
	nounN = random.randint(0, numnouns) #picks a random line number
	verbN = random.randint(0, numverbs) #picks a random line number
	adjN  = random.randint(0, numadjs)  #picks a random line number
	
	#will pick a sentence to pick and use for its tweets
	
	if (seqnum == 0 or seqnum == 5):
		tweet = "Tom, why did you " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + "? "	
	if (seqnum == 1 or seqnum == 6):
		tweet = "Tom got " + verbs[verbN] + " by a " + adjs[adjN] + " " + nouns[nounN] + ". "
	if (seqnum == 2 or seqnum == 7):
		tweet = "Don't " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + ", Tom! "
	if (seqnum == 3 or seqnum == 8):
		tweet = "Tom decided to " + verbs[verbN] + " a " + adjs[adjN] + " " + nouns[nounN] + " "
	if (seqnum == 4 or seqnum == 9):
		tweet = "Tom asked " + adjs[adjN] + " " + nouns[nounN] + " to be his #Valentine."	
	tweet = re.sub('\s+',' ',tweet) #Removes whitespaces and replaces them with spaces
	tweet = tweet + " #YOLO"					
	return tweet





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
	while(administrativeTweet <=9):		
		print "tweeting normal tweet"
		text=newtweet(administrativeTweet)
		administrativeTweet = administrativeTweet+1
		print text
		time.sleep(20)#waits 20 secs to kill program if need be
		api.update_status(status=text)
		print " "
		print "tweeted"
		time.sleep(1780)#Tweet every 30 minutes
	if(administrativeTweet>9):
		print "tweeting admin tweet"
		print " "
		current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		api.update_status(status='Made by Dan J. and Leo T. for #Codeday 2015 Feb 14th'+current_time)
		administrativeTweet=0	
		time.sleep(1800)#Tweet every 30 minutes        
	if (administrativeTweet==-1):
		api.get_user('tompaulus')
	
