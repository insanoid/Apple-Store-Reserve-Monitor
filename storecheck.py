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

## 
reload(sys)
sys.setdefaultencoding('utf-8')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\0330m'

# Change this to alter the monitoring stores.
pref_stores = ['R358', 'R396', 'R352']


# Change the country and language for your location.
storeurl = "https://reserve.cdn-apple.com/DE/de_DE/reserve/iPhone/stores.json"
availurl = "https://reserve.cdn-apple.com/DE/de_DE/reserve/iPhone/availability.json"


def decode(k):

    # Incase of a new version, update models here.
    model_mapping  = {
        "MN962ZD/A": "iPhone 7 Jet Black - 128 GB",
        "MN9C2ZD/A": "iPhone 7 Jet Black - 256 GB",
        "MN8X2ZD/A": "iPhone 7 Black - 32 GB",
        "MN922ZD/A": "iPhone 7 Black - 128 GB",
        "MN972ZD/A": "iPhone 7 Black - 256 GB",
        "MN902ZD/A": "iPhone 7 Gold - 32 GB",
        "MN942ZD/A": "iPhone 7 Gold - 128 GB",
        "MN992ZD/A": "iPhone 7 Gold - 256 GB",
        "MN912ZD/A": "iPhone 7 Rose Gold - 32 GB",
        "MN952ZD/A": "iPhone 7 Rose Gold - 128 GB",
        "MN9A2ZD/A": "iPhone 7 Rose Gold - 256 GB",
        "MN8Y2ZD/A": "iPhone 7 Silver - 32 GB",
        "MN932ZD/A": "iPhone 7 Silver - 128 GB",
        "MN982ZD/A": "iPhone 7 Silver - 256 GB",
        "MN4V2ZD/A": "iPhone 7 Plus Jet Black - 128 GB",
        "MN512ZD/A": "iPhone 7 Plus Jet Black - 256 GB",
        "MNQM2ZD/A": "iPhone 7 Plus Black - 32 GB",
        "MN4M2ZD/A": "iPhone 7 Plus Black - 128 GB",
        "MN4W2ZD/A": "iPhone 7 Plus Black - 256 GB",
        "MNQQ2ZD/A": "iPhone 7 Plus Rose Gold - 32 GB",
	"MN4U2ZD/A": "iPhone 7 Plus Rose Gold- 128 GB",
	"MN4Y2ZD/A": "iPhone 7 Plus Rose Gold - 256 GB",
	"MNQP2ZD/A": "iPhone 7 Plus Gold - 32 GB",
        "MN4Q2ZD/A": "iPhone 7 Plus Gold - 128 GB",
        "MN502ZD/A": "iPhone 7 Plus Gold - 256 GB",
        "MNQN2ZD/A": "iPhone 7 Plus Silver - 32 GB",
        "MN4P2ZD/A": "iPhone 7 Plus Silver - 128 GB",
        "MN4X2ZD/A": "iPhone 7 Plus Silver - 256 GB",
		"timeSlot":""
    }

    model_name = model_mapping.get(k)
    if(len(model_name) <= 0):
        model_name = k

    return  bcolors.FAIL + model_name



store_json = requests.get(storeurl).json()
avail_json = requests.get(availurl).json()
avail = False
avail_in_required = False;

if 'stores' in store_json:
    for key in store_json['stores']:
        items =  avail_json.get(key.get('storeNumber'))
        print bcolors.OKGREEN + str(key.get('storeName')) + ", " + str(key.get('storeCity'))
        items_available = False
        for k in items:
            if items[k] == True:
                print bcolors.OKGREEN + "    -    " + decode(k)
                avail = True;
                if key.get('storeNumber') in pref_stores:
                    avail_in_required = True;
        if items_available == False:
            print bcolors.FAIL + "Nothing Available\n"
    print bcolors.OKBLUE + "Updated: "+ time.strftime('%d, %b %Y %H:%M:%S')  + "\n"
    if avail_in_required == True:
        os.system('say -v "Veena" "iPhone\ is Available in the required store!!."')

else:
    print bcolors.FAIL + time.strftime('%d, %b %Y %H:%M:%S') + " - Data Unavailable."
