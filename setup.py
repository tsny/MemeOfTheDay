from os import path
import sys, json, os

def ValidateFiles():
    if not (path.isfile('settings.json')):
        FirstTimeSetup()

    if not (path.exists('./memes')):
        print('Could not find memes folder')
        exit()

def FirstTimeSetup():
    print("Running first time setup, get your Consumer/Access keys from apps.twitter.com")

    consumerKey = input("Enter your consumer key: ")
    consumerSecret = input("Enter your consumer secret: ")
    accessKey = input("Enter your access key: ")
    accessSecret = input("Enter your access secret: ")
    
    data =  { 'loginDetails':  
                {
                    'consumerKey' : consumerKey,
                    'consumerSecret' : consumerSecret,
                    'accessKey' : accessKey,
                    'accessSecret' : accessSecret}
                }

    with open('settings.json', 'x') as outfile:
        json.dump(data, outfile, indent=4)

    return 