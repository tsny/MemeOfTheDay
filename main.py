#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random, os, json, argparse
from setup import ValidateFiles, FirstTimeSetup


def FindTodaysMeme():
    """ 
    Finds the filename of a random meme to post

    Returns:
        str: relative file path to random .png/.jpg file
    """

    path = r"./memes/"

    try:
        randomFilename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x)) and
            x.endswith('.png') or x.endswith('.jpg')
        ])

    except:
        print("Couldn't find an image in ./memes")
        exit()

    print("Got image:  " + randomFilename)

    return path + randomFilename

def Login():
    """
    Opens settings.json and authenticates Consumer/Access Keys via tweepy

    Returns:
        API handle
    """

    with open(r"./settings.json") as data_file:
        data = json.load(data_file)

    CONSUMER_KEY = data["loginDetails"]["consumerKey"]
    CONSUMER_SECRET = data["loginDetails"]["consumerSecret"]
    ACCESS_KEY = data["loginDetails"]["accessKey"]
    ACCESS_SECRET = data["loginDetails"]["accessSecret"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        print("Logged in as " + api.me().name)

    except:
        print("Credentials invalid; Update settings.json...")
        exit()

    return api

def CheckForArgs():
    '''
    Adds arguments to program
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true', help='Test the login. Does not post to Twitter.')
    parser.add_argument('-km', '--keep', action='store_true', help='Do not delete the meme after posting.')
    parser.add_argument('-sp', '--setup', action='store_true', help='Delete settings.json if it exists and get consumer/access keys from user.')

    return parser.parse_args()

def Main():
    args = CheckForArgs()

    if(args.setup):
        os.remove('settings.json')
        FirstTimeSetup()

    ValidateFiles()
    api = Login()
    todaysMeme = FindTodaysMeme()

    if(args.test):
        print("This was a test run... Nothing was posted")
        exit()

    api.update_with_media(todaysMeme, "#memeoftheday")

    if(args.keep):
        print("keeping file...")
        exit()

    os.remove(todaysMeme)

if __name__ == "__main__":
    Main()