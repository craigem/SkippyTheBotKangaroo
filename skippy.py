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
from BeautifulSoup import UnicodeDammit
# Import regular expression capabilities
import re

# Have the bot join IRC
# Import some necessary libraries.
import socket 

# Some basic variables used to configure the bot        
server = "irc.freenode.net" # Server
channel = "#STBK" # Channel
botnick = "STBK" # Your bots nick


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def whatsup(): # This function responds to a user that inputs "What's up Skip?"
  ircsock.send("PRIVMSG "+ channel +" :Is that you Sonny?\n")

def getPage(url):
	"""Gets a URL from IRC reads it"""
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

ircmsg = ircsock.recv(2048) # receive data from the server
ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.

while ircmsg.find(channel) == -1:
	ircmsg = ircsock.recv(2048) # receive data from the server
	ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.

while 1: # Be careful with these! it might send you to an infinite loop
	ircmsg = ircsock.recv(2048) # receive data from the server
	ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
	print(ircmsg) # Here we print what's coming from the server

	# Extract the title from the page and print it
	# if ircmsg.find ("http") != -1:
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ircmsg)
	if len(url) > 0:
		try:
			titlePage = BeautifulSoup(getPage(url[0]))
			for  child in titlePage.title:
				sendmsg(channel, "Title: "+ child.encode("utf-8"))
		except urllib2.HTTPError, e:
			sendmsg(channel, "I can't find that page Sonny!")
		

	if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
		hello()

	if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
		ping()

	if ircmsg.find(":What's up Skip?") != -1: # If we can find "What's Up Skip" it will call the function whatsup()
		whatsup()

# Read the channel for URLS
# Feed the URLs into the below functions

