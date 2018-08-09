#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from pathHelper import ValidateFiles
import time, sys, random, os, json, argparse
from os import path

# Finds the filename of a random meme to post

def FindTodaysMeme():
    path = r"./memes/"

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

    with open(r"./login.json") as data_file:
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

def CheckForArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true', help='Test the login. Does not post to Twitter.')
    parser.add_argument('-km', '--keep', action='store_true', help='Do not delete the meme after posting.')

    return parser.parse_args()

def Main():
    ValidateFiles()
    api = Login()
    todaysMeme = FindTodaysMeme()

    args = CheckForArgs()

    if(args.test):
        print("This was a test run... Nothing was posted")
        exit()

    UpdateStatus(api, todaysMeme)

    if(args.keep):
        print("keeping file...")
        exit()

    os.remove(todaysMeme)

def UpdateStatus(apiHandle, image):
    apiHandle.update_with_media(image, "#memeoftheday")

# --- MAIN --- 

Main()
