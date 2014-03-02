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

#def getURL():
#	"""Gets a URL from RAW INPUT and prints it"""
#	url = raw_input("Feed me a URL: ")
#	print "%s" % url
#	"""Take the same URL and get the headers"""
#	URLheaders = urllib.urlopen(url)
#	print "%s" % URLheaders

# getURL()

def getPage():
	url = raw_input("Feed me a URL: ")
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
 
if __name__ == "__main__":
	namesPage = getPage()
	print namesPage
