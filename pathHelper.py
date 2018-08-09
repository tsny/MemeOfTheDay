from os import path

def ValidateFiles():
    if not (path.isfile('login.json')):
        raise FileNotFoundError('Could not find login details')

    if not (path.exists('./memes')):
        raise FileNotFoundError('Could not find memes folder')