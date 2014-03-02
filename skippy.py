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

def getPage():
	"""Gets a URL from RAW INPUT and reads it"""
	url = raw_input("Feed me a URL: ")
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
 
# Extract the title from the page and print it
if __name__ == "__main__":
	titlePage = BeautifulSoup(getPage())
	print "%s" % titlePage.title
