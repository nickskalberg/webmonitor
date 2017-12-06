import urllib2
import threading
import datetime
from decimal import *

webinput = raw_input("Website: http://")
url = ("www." + webinput)
print "Connecting to http://" + url + "..."
webUrl = urllib2.urlopen("http://" + webinput)

if str(webUrl.getcode()) == "200":
	print "Connection successful."

def ratefunc():
	rate1 = input("Scraping rate (minimum 3 seconds): ")
	if rate1 < 3:
		ratefunc()
	return rate1

rate2 = '{:.1f}'.format(ratefunc())
rate = float(rate2)
x = 0

def check():

	global x
	threading.Timer(rate, check).start()
	webUrl = urllib2.urlopen("http://" + webinput)
	if x == 0:
		global starttime
		starttime = datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
		global startdata
		startdata = webUrl.read()
		x = 1

	if starttime != datetime.datetime.now().strftime("%m-%d-%Y %I:%M %p"):
		data = webUrl.read()
		if data != startdata:
			print "Change made at " + datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
			startdata = data

check()
