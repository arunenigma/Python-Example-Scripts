import sys
import re
import urllib2
def get_alexa_rank(url):
	try:
		data = urllib2.urlopen('http://google.com' % (url)).read()
		reach_rank = re.findall("REACH[^\d]*(\d+)",data)
		:
