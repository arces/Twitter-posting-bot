import random, re
random.seed()

i = 0
nouns =s = i

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
	nounN = random.randint(0, numnouns)
	verbN = random.randint(0, numverbs)
	adjN  = random.randint(0, numadjs)
	if (seqnum == 0 or seqnum == 5):
		tweet = "Tom, why did you " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + "? "	
	if (seqnum == 1 or seqnum == 6):
		tweet = "Tom got " + verbs[verbN] + " by a " + adjs[adjN] + " " + nouns[nounN] + "."
	if (seqnum == 2 or seqnum == 7):
		tweet = "Don't " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + ", Tom!"
	if (seqnum == 3 or seqnum == 8):
		tweet = "Tom decided to " + verbs[verbN] + " a " + adjs[adjN] + " " + nouns[nounN]	
	if (seqnum == 4 or seqnum == 9):
		tweet = "Tom asked " + adjs[adjN] + " " + nouns[nounN] + " to be his #Valentine."	
	tweet = re.sub('\s+',' ',tweet) #Removes whitespaces and replaces them with spaces
	tweet = tweet + "@TomPaulus #CodeDay"					
	return tweet

print newtweet(0) []
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
	nounN = random.randint(0, numnouns)
	verbN = random.randint(0, numverbs)
	adjN  = random.randint(0, numadjs)
	if (seqnum == 0 or seqnum == 5):
		tweet = "Tom, why did you " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + "? "	
	if (seqnum == 1 or seqnum == 6):
		tweet = "Tom got " + verbs[verbN] + " by a " + adjs[adjN] + " " + nouns[nounN] + "."
	if (seqnum == 2 or seqnum == 7):
		tweet = "Don't " + verbs[verbN] + " that " + adjs[adjN] + " " + nouns[nounN] + ", Tom!"
	if (seqnum == 3 or seqnum == 8):
		tweet = "Tom decided to " + verbs[verbN] + " a " + adjs[adjN] + " " + nouns[nounN]	
	if (seqnum == 4 or seqnum == 9):
		tweet = "Tom asked " + adjs[adjN] + " " + nouns[nounN] + " to be his #Valentine."	
	tweet = re.sub('\s+',' ',tweet) #Removes whitespaces and replaces them with spaces
	tweet = tweet + "@TomPaulus #CodeDay"					
	return tweet

print newtweet(0)
