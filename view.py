#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from setup import *


def CreateInputBoxes(window):

    creds = GetCredentialsFromFile()

    label = Label(window, text="Consumer Key")
    label.pack()

    text = Entry(window, width=25)
    text.insert(0, creds[0])
    text.pack()

    label = Label(window, text="Consumer Secret")
    label.pack()

    text = Entry(window, width=25)
    text.insert(0, creds[1])
    text.pack()

    label = Label(window, text="Access Key")
    label.pack()

    text = Entry(window, width=25)
    text.insert(0, creds[2])
    text.pack()

    label = Label(window, text="Access Secret")
    label.pack()

    text = Entry(window, width=25)
    text.insert(0, creds[3])
    text.pack(pady = (0,30))

    return


def CreateWindow():

    window = Tk()
    window.title("Settings")
    window.geometry("250x400")

    CreateInputBoxes(window)

    def revert():
        print("Reverted settings...")

    def quitCommand():
        window.quit()

    def saveMessageBox():
        res = messagebox.askyesno('Save Confirmation',
                                  'Are you sure you want to save this configuration?')
        # Do stuff here with user response

    Button(window, text="Post Meme", command=quitCommand).pack()
    Button(window, text="Save Settings", command=quitCommand).pack()
    Button(window, text="Revert Settings", command=quitCommand).pack()
    Button(window, text="Quit", command=quitCommand).pack()

    window.mainloop()

    return window

def Main():
    window = CreateWindow()

if __name__ == "__main__":
    Main()
