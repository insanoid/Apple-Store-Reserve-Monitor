#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from __future__ import print_function, unicode_literals

import os
import time
import sys
import requests
import json
import minibar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\0330m'

## Base URL is the apple's URL used to make product links and also API calls. Country code only for non-US countries.
base_url = "https://www.apple.com/{0}/"
## End point for searching for all possible product combinations in the given product family.
product_locator_url = "{0}shop/product-locator-meta?family={1}"
## End point for searching for pickup state of a certain model at a certain location.
product_availability_url = "{0}shop/retail/pickup-message?pl=true&parts.0={1}&location={2}"

## Load the configration from the config, country, device family, zip, models to search for etc.
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

country_code = config.get('country_code')
device_family = config.get('device_family')
zip_code = config.get('zip_code', [])
selected_device_models = config.get('models', [])
selected_carriers = config.get('carriers', [])
selected_stores = config.get('stores', [])

## Since the URL only needs country code for non-US countries, switch the URL for country == US.
if country_code.upper() == 'US':
    base_url = "https://www.apple.com/"
else:
    base_url = base_url.format(country_code)

## Store the information about the available devices for the family - title, model, carrier.
device_list = []

## Downloading the list of products from the server for the current device family.
print('{}➜  Downloading Models List...'.format(bcolors.OKBLUE))

product_locator_response = requests.get(product_locator_url.format(base_url, device_family))
if product_locator_response.status_code == 200:
    product_list = product_locator_response.json().get('body').get('productLocatorOverlayData').get('productLocatorMeta').get('products')
    ## Take out the product list and extract only the useful information.
    for product in product_list:
        model = product.get('partNumber')
        carrier = product.get('carrierModel')
        ## Only add the requested models and requested carriers (device models are partially matched)
        if (any(item in model for item in selected_device_models) or len(selected_device_models) == 0) and (carrier in selected_carriers or len(selected_carriers) == 0):
            device_list.append({'title': product.get('productTitle'), 'model': model, "carrier": carrier})

## Exit if no device was found.
if len(device_list) == 0:
    print('{}✖  No device matching your configuration was found!'.format(bcolors.FAIL))
    exit(1)
else:
    print('{}✔  Found {} devices matching your config.'.format(bcolors.OKGREEN, len(device_list)))

## Downloading the list of products from the server.
print('{}➜  Downloading Stock Information for the devices...\n'.format(bcolors.OKBLUE))

stores_list_with_stock = {}
for device in minibar.bar(device_list):
    product_availability_response = requests.get(product_availability_url.format(base_url, device.get('model'), zip_code))
    store_list = product_availability_response.json().get('body').get('stores')

    ## Go through all the stores in the list and extract useful information.
    ## Group products by store (put the stock for this device in the store's parts attribute)
    for store in store_list:
        current_store = stores_list_with_stock.get(store.get('storeNumber'))
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

        ## If the store is in the list of user's preferred list, add it to the list to check for stock.
        if (store.get('storeNumber') in selected_stores or len(selected_stores) == 0):
            stores_list_with_stock[store.get('storeNumber')] = current_store

## Get all the stores and sort it by the sequence.
stores = list(stores_list_with_stock.values())
stores.sort(key=lambda k : k['sequence'])

## Boolean indicating if the stock is available for any of the items requested (used to play the sound)
stock_available = False

## Go through the stores and fetch the stock for all the devices/parts in the store and print their status.
for store in stores:
    print('\n\n{}{}, {} ({})'.format(bcolors.OKGREEN, store.get('storeName'), store.get('city'), store.get('storeId')))
    for part_id, part in store.get('parts').items():
        if part.get('storeSelectionEnabled') is True:
            stock_available = True
            print(u"{} - {} ({})".format(bcolors.OKBLUE, part.get('storePickupProductTitle'), part.get('partNumber')))
        else:
            print(u"{} - {} ({})".format(bcolors.FAIL, part.get('storePickupProductTitle'), part.get('partNumber')))

## Play the sound if phone is available.
if stock_available:
    os.system('say "Device Available!"')
print('\n\n')
