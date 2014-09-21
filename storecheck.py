# The MIT License (MIT)
# Copyright (c) 2014 Karthikeya Udupa KM
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import urllib
import urllib2
import httplib
import sys
import datetime
from dateutil import parser
from bs4 import BeautifulSoup
import requests
import os
import time

#change this to alter the monitoring stores.
pref_stores = ['R118', 'R410', 'R270', 'R255','R092']
	
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
def decode(k):

	if(k=="MG4J2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Silver - 128GB"
	elif(k=="MGAJ2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Silver - 64GB"
	elif(k=="MGA82B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Silver - 16GB"

	elif(k=="MGAC2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Grey - 128GB"
	elif(k=="MGAH2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Grey - 64GB"

	elif(k=="MGAF2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Gold - 128GB"
	elif(k=="MGAK2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Gold - 64GB"
	elif(k=="MGAA2B/A"):
		return bcolors.FAIL + "Apple iPhone 6 Plus Gold - 16GB"

	elif(k=="MG4H2B/A"):
		return bcolors.FAIL + "MG4H2B/A"

	elif(k=="MG4J2B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Gold - 64GB"
	elif(k=="MG492B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Gold - 16GB"
	elif(k=="MG4E2B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Gold - 128GB"
	elif(k=="MG4F2B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Grey - 64GB"
	elif(k=="MG472B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Grey - 16GB"
	elif(k=="MG4A2B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Grey - 128GB"
	elif(k=="MG4C2B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Silver - 128GB"
	elif(k=="MG482B/A"):
		return bcolors.WARNING + "Apple iPhone 6 Silver - 16GB"

	else:
		return bcolors.FAIL + k;

    
storeurl = "https://reserve.cdn-apple.com/GB/en_GB/reserve/iPhone/stores.json"
availurl = "https://reserve.cdn-apple.com/GB/en_GB/reserve/iPhone/availability.json"


try:
	store_json = requests.get(storeurl).json()
	avail_json = requests.get(availurl).json()

	avail = False
	avail_in_required = False;

	if 'stores' in store_json:
		for key in store_json['stores']:
			items =  avail_json[key['storeNumber']]
			print bcolors.OKGREEN + str(key['storeName'])
			for k in items:
				if items[k]==True:
					print bcolors.OKGREEN + "	-	" + decode(k)
					avail = True;
					if key['storeNumber'] in pref_stores:
						avail_in_required = True;
		print bcolors.OKBLUE + "Updated: "+ time.strftime('%d, %b %Y %H:%M:%S')  + "\n"
		if avail_in_required == True:
			os.system('say -v "Kate" "iPhone\ is Available in the required store!!."')

	else:
		print bcolors.FAIL + time.strftime('%d, %b %Y %H:%M:%S') + " - Data Unavailable."
except ValueError:
	print bcolors.FAIL + time.strftime('%d, %b %Y %H:%M:%S')  + " - Server Unavailable."
