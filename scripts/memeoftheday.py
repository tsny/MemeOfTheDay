#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random, os, json
 
# Finds the filename of a random meme to post
def FindTodaysMeme():
	path = r"/home/tsny/MemeOfTheDay/memes/"

	try:
		randomFilename = random.choice([
			x for x in os.listdir(path)
			if os.path.isfile(os.path.join(path, x)) and
			x.endswith('.png') or x.endswith('.jpg')
		])

	except:
		print("Couldn't find an image")
		exit()

	print("Got image:  " + randomFilename)

	return path + randomFilename

# Returns api handle
def Login():

	with open(r"/home/tsny/MemeOfTheDay/login/loginDetails.json") as data_file:
		data = json.load(data_file)

	CONSUMER_KEY = data["loginDetails"]["consumerKey"]
	CONSUMER_SECRET = data["loginDetails"]["consumerSecret"]
	ACCESS_KEY = data["loginDetails"]["accessKey"]
	ACCESS_SECRET = data["loginDetails"]["accessSecret"]

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	return api

# Test Func that came with source, opens a file and posts something, ignore this
def TestFunc():
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()
     
    for line in f:
        api.update_status(line)
        time.sleep(900)#Tweet every 15 minutes

def UpdateStatus(apiHandle, image):
    apiHandle.update_with_media(image, "#memeoftheday")

# --- MAIN --- 

api = Login()
todaysMeme = FindTodaysMeme()

try:
	firstArg = sys.argv[1]

except:
	print("This was a test run. Add -r to post to Twitter")
	exit()

else:
	UpdateStatus(api, todaysMeme)
	os.remove(todaysMeme)
