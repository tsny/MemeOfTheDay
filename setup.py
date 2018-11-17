from os import path
import sys, json, os

def ValidateFiles():
    if not (path.isfile('settings.json')):
        ManualCredEntry()

    if not (path.exists('./memes')):
        print('Could not find memes folder')
        exit()

    return

def ManualCredEntry():

    print("Please manually enter your twitter credentials...")

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

def WriteToSettingsFile(input):

    data =  { 'loginDetails':  
                {
                    'consumerKey' : consumerKey,
                    'consumerSecret' : consumerSecret,
                    'accessKey' : accessKey,
                    'accessSecret' : accessSecret}
                }
        
def GetCredentialsFromFile():

    try:
        data_file = open(r"./settings.json")
        data = json.load(data_file)

    except IOError:
        print("ERROR: Couldn't find settings.json")
        ManualCredEntry()

    CONSUMER_KEY = data["loginDetails"]["consumerKey"]
    CONSUMER_SECRET = data["loginDetails"]["consumerSecret"]
    ACCESS_KEY = data["loginDetails"]["accessKey"]
    ACCESS_SECRET = data["loginDetails"]["accessSecret"]

    creds = [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET]

    data_file.close()

    return creds

