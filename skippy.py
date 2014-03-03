#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A poorly written python IRC bot

@author Craige McWhirter (craige@mcwhirter.com.au)
@copyright Copyright (c) 2014 Craige McWhirter
@License GPLv3
"""

# Import the sys library
import sys
# Import common operations on POSIX pathnames
import os.path
# Import functions to manipulate time values
import time
# Import the ability to open URLs
import urllib2
# Import the ability to match filenames with shell patterns
import fnmatch
# Import the basis for parsing text files formatted in HTML
import HTMLParser
# Import the capability to do logging
import logging
# Import additional logging handlers
import logging.handlers
# Import a nifty HTML parser
from BeautifulSoup import BeautifulSoup
#from util.BeautifulSoup import UnicodeDammit

# Have the bot join IRC
# Import some necessary libraries.
import socket 

# Some basic variables used to configure the bot        
server = "irc.freenode.net" # Server
channel = "#taslug" # Channel
botnick = "STBK" # Your bots nick


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()
# Read the channel for URLS
# Feed the URLs into the below functions

def getPage():
	"""Gets a URL from RAW INPUT and reads it"""
	url = raw_input("Feed me a URL: ")
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
 
# Extract the title from the page and print it
if __name__ == "__main__":
	titlePage = BeautifulSoup(getPage())
	for  child in titlePage.title:
		print(child)
