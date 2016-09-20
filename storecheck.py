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

import requests
import os
import time
import sys

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

# Change this to alter the monitoring stores and devices
pref_stores = ['R358', 'R396', 'R352', 'R659']
pref_models = ['MN4M2', 'MN972']


# Change the country and language for your location for example (DE/de_DE, GB/en_GB)
storeurl = "https://reserve.cdn-apple.com/DE/de_DE/reserve/iPhone/stores.json"
availurl = "https://reserve.cdn-apple.com/DE/de_DE/reserve/iPhone/availability.json"


# Incase of a new version, update models here.
model_mapping  = {
    "MN962": "iPhone 7 Jet Black - 128 GB",
    "MN9C2": "iPhone 7 Jet Black - 256 GB",
    "MN8X2": "iPhone 7 Black - 32 GB",
    "MN922": "iPhone 7 Black - 128 GB",
    "MN972": "iPhone 7 Black - 256 GB",
    "MN902": "iPhone 7 Gold - 32 GB",
    "MN942": "iPhone 7 Gold - 128 GB",
    "MN992": "iPhone 7 Gold - 256 GB",
    "MN912": "iPhone 7 Rose Gold - 32 GB",
    "MN952": "iPhone 7 Rose Gold - 128 GB",
    "MN9A2": "iPhone 7 Rose Gold - 256 GB",
    "MN8Y2": "iPhone 7 Silver - 32 GB",
    "MN932": "iPhone 7 Silver - 128 GB",
    "MN982": "iPhone 7 Silver - 256 GB",
    "MN4V2": "iPhone 7 Plus Jet Black - 128 GB",
    "MN512": "iPhone 7 Plus Jet Black - 256 GB",
    "MNQM2": "iPhone 7 Plus Black - 32 GB",
    "MN4M2": "iPhone 7 Plus Black - 128 GB",
    "MN4W2": "iPhone 7 Plus Black - 256 GB",
    "MNQQ2": "iPhone 7 Plus Rose Gold - 32 GB",
    "MN4U2": "iPhone 7 Plus Rose Gold- 128 GB",
    "MN4Y2": "iPhone 7 Plus Rose Gold - 256 GB",
    "MNQP2": "iPhone 7 Plus Gold - 32 GB",
    "MN4Q2": "iPhone 7 Plus Gold - 128 GB",
    "MN502": "iPhone 7 Plus Gold - 256 GB",
    "MNQN2": "iPhone 7 Plus Silver - 32 GB",
    "MN4P2": "iPhone 7 Plus Silver - 128 GB",
    "MN4X2": "iPhone 7 Plus Silver - 256 GB",
	"timeSlot":""
}

store_json = requests.get(storeurl).json()
avail_json = requests.get(availurl).json()

avail_in_required = False

if 'stores' in store_json:
    for store in store_json['stores']:
        items =  avail_json.get(store.get('storeNumber'))
        store_in_prefer = store.get('storeNumber') in pref_stores
        if store_in_prefer:
            print('{}{}, {} ({})'.format(bcolors.OKGREEN, store.get('storeName'), store.get('storeCity'), store.get('storeNumber')))
        items_available = False
        for model_code in items:
            if items.get(model_code) != "NONE":
                partial_model_code = model_code[0:5]
                model_name = model_mapping.get(partial_model_code, None)
                if model_name != None:
                    items_available = True;
                    if store_in_prefer and partial_model_code in pref_models:
                        avail_in_required = True;
                        print('{}    -    {}'.format(bcolors.FAIL, model_name))
                    elif store_in_prefer:
                        print('{}    -    {}'.format(bcolors.OKBLUE, model_name))

        if not items_available and store_in_prefer:
            print('{}Nothing Available\n'.format(bcolors.FAIL))
    print('{}Updated: {}\n'.format(bcolors.OKBLUE, time.strftime('%d, %b %Y %H:%M:%S')))

    if avail_in_required:
        os.system('say "iPhone is Available in the required store."')

else:
    print('{}Data Unavailable: {}\n'.format(bcolors.OKBLUE, time.strftime('%d, %b %Y %H:%M:%S')))
