#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Test Comment
 
import tweepy, time, sys, random, os, json, argparse

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

    print("Login successful")

	return api

# Test Func that came with source, opens a file and posts something, ignore this
def TestFunc():
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()
     
    for line in f:
        api.update_status(line)
        time.sleep(900)#Tweet every 15 minutes

def CheckForArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--test', action='store_true', help='Test the login. Does not post to Twitter.')
	parser.add_argument('-km', '--keep', action='store_true', help='Do not delete the meme after posting.')

	return parser.parse_args()

def Main():
    api = Login()
    todaysMeme = FindTodaysMeme()

    args = CheckForArgs()

    if(args.test):
        print("This was a test run... Nothing was posted")
        exit()

    UpdateStatus(api, todaysMeme)
    os.remove(todaysMeme)

def UpdateStatus(apiHandle, image):
    apiHandle.update_with_media(image, "#memeoftheday")

# --- MAIN --- 

Main()
