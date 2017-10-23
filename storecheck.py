#!/usr/bin/env python

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

import os
import time
import sys
import requests
from clint.textui import progress


reload(sys)
sys.setdefaultencoding('utf-8')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\0330m'

country_code = "gb"
device_family = "iphone8"
zip_code = "B152RB"

product_locator_url = "https://www.apple.com/{0}/shop/product-locator-meta?family={1}"
product_availability_url = "https://www.apple.com/{0}/shop/retail/pickup-message?pl=true&parts.0={1}&location={2}"

# Store title, model, carrier in an array to travese later.
model_info = []

# Downloading the list of products from the server.
print('{} Downloading Models List...'.format(bcolors.WARNING))
product_list_response = requests.get(product_locator_url.format(country_code, device_family), stream=True)

if product_list_response.status_code == 200:
    product_list = product_list_response.json().get('body').get('productLocatorOverlayData').get('productLocatorMeta').get('products')
    for product in product_list:
        model_info.append({'title': product.get('productTitle'), 'model': product.get('partNumber'), "carrier": product.get('carrierModel')})

# Downloading the list of products from the server.
print('{} Downloading Stock Information...'.format(bcolors.WARNING))

store_stock_info = {}
for product in model_info:
    product_response = requests.get(product_availability_url.format(country_code, product.get('model'), zip_code), stream=True)
    store_list = product_response.json().get('body').get('stores')
    for store in store_list:
        current_store = store_stock_info.get(store.get('storeNumber'))
        if current_store is None:
            current_store = {
                'storeId': store.get('storeNumber'),
                'storeName': store.get('storeName'),
                'city': store.get('city'),
                'sequence': store.get('storeListNumber'),
                'parts': {}
            }
        new_parts = store.get('partsAvailability')
        old_parts = current_store.get('parts')
        old_parts.update(new_parts)
        current_store['parts'] = old_parts
        store_stock_info[store.get('storeNumber')] = current_store

stores = store_stock_info.values()
stores.sort(key=lambda k : k['sequence'])
for store in stores:
    print('{}{}, {} ({})'.format(bcolors.OKGREEN, store.get('storeName'), store.get('city'), store.get('storeId')))
    for part_id, part in store.get('parts').items():
        if part.get('storeSelectionEnabled') is True:
            print(" - {} {}".format(bcolors.OKBLUE, part.get('storePickupProductTitle')))
        else:
            print(" - {} {}".format(bcolors.FAIL, part.get('storePickupProductTitle')))
