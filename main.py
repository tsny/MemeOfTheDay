#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys
import random
import os
import json
import argparse
from setup import *
from view import *


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
        print("ERROR: Couldn't find an image in ./memes")
        exit()

    print("Got image:  " + randomFilename)

    return path + randomFilename


def Login():
    """
    Opens settings.json and authenticates Consumer/Access Keys via tweepy

    Returns:
        API handle
    """

    creds = GetCredentialsFromFile()

    auth = tweepy.OAuthHandler(creds[0], creds[1])
    auth.set_access_token(creds[2], creds[3])
    api = tweepy.API(auth)

    try:
        print("Logged in as " + api.me().name)

    except:
        print("ERROR: Credentials invalid; Check settings.json...")
        exit()

    return api


def CheckForArgs():
    '''
    Adds arguments to program
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--manual', action='store_true', help="MANUAL. Run this to manually write your creds to settings.json via cmd line")
    parser.add_argument('-t', '--test', action='store_true',
                        help='TEST. Test the login. Does not post to Twitter.')
    parser.add_argument('-km', '--keep', action='store_true',
                        help='KEEP MEME. Do not delete the meme after posting.')
    parser.add_argument('-sp', '--setup', action='store_true',
                        help='SETUP. Delete settings.json if it exists and get consumer/access keys from user.')

    return parser.parse_args()


def Main():
    args = CheckForArgs()

    if(args.setup):
        CreateWindow()

    ValidateFiles()
    api = Login()
    todaysMeme = FindTodaysMeme()

    if(args.test):
        print("This was a test run... Nothing was posted")
        exit()

    api.update_with_media(todaysMeme, "#memeoftheday")

    if(args.keep):
        print("Keeping meme...")
        exit()

    os.remove(todaysMeme)

    return

if __name__ == "__main__":
    Main()
