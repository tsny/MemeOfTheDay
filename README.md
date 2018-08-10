# MemeOfTheDay
This time without free API keys! I PROMISE

A simple python project that posts a random meme from a supply on my server to my Twitter every day at 6 PM.

And yes those API keys from that first commit no longer work.

***

### Usage:

1) Clone this repo
2) Create a folder in this repo called 'memes'
3) Put a .jpg or .png in the new 'memes' folder
4) Run the program for the first time or create a file called 'login.json'
4a) If you're creating the json file by hand: write your Consumer and Access keys and secrets into it in this format:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"loginDetails":  
&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"consumerKey": "gasgasgsgsadgagasg",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"consumerSecret": "gasdgasdftew geagasgsdagsdg",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"accessKey": "4343262-gsadgsdfasdfewaysyta",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"accessSecret": "6t34634fdsafdsaffdsfasfsdaf"  
&nbsp;&nbsp;&nbsp;&nbsp;}  
}  

6) Run memeoftheday.py

***

### Arguments:

-t, --test  
Runs a test of the login, does not post to twitter

-kp, --keep  
Does not delete meme after posting it

-sp, --setup  
Deletes the settings.json file if it exists and gets the consumer/access keys from the user's input
