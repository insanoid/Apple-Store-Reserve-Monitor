#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import json
import os
import sys
import time
from datetime import datetime

import crayons
import minibar
import requests


class Configuration:
    """Load the configuration from the config, country, device family, zip, models to search for."""

    def __init__(self, filename):
        if filename is None:
            print("No configuration was provided.")
            exit(0)
        with open("config.json") as json_data_file:
            config = json.load(json_data_file)

        self.country_code = config.get("country_code")
        self.device_family = config.get("device_family")
        self.zip_code = config.get("zip_code", [])
        self.selected_device_models = config.get("models", [])
        self.selected_carriers = config.get("carriers", [])
        self.selected_stores = config.get("stores", [])
        # Store numbers are available here.
        self.appointment_stores = config.get("appointment_stores", [])


class StoreChecker:
    """Class to handle store checking and fetching and processing of stock of apple products."""

    # Base URL is the apple's URL used to make product links and also API
    # calls. Country code is needed only for non-US countries.
    APPLE_BASE_URL = "https://www.apple.com/{0}/"
    # End point for searching for all possible product combinations in the
    # given product family.
    PRODUCT_LOCATOR_URL = "{0}shop/product-locator-meta?family={1}"
    # End point for searching for pickup state of a certain model at a certain
    # location.
    PRODUCT_AVAILABILITY_URL = "{0}shop/retail/pickup-message?pl=true&parts.0={1}&location={2}"
    # URL for the store availabile
    STORE_APPOINTMENT_AVAILABILITY_URL = (
        "https://retail-pz.cdn-apple.com/product-zone-prod/availability/{0}/{1}/availability.json"
    )

    def __init__(self, filename="config.json"):
        """Initialize the configuration for checking store(s) for stock."""

        self.configuration = Configuration(filename)
        self.stores_list_with_stock = {}
        self.base_url = "https://www.apple.com/"

        # Since the URL only needs country code for non-US countries, switch
        # the URL for country == US.
        if self.configuration.country_code.upper() != "US":
            self.base_url = self.APPLE_BASE_URL.format(self.configuration.country_code)

    def refresh(self):
        """Refresh information about the stock that is available on the Apple website."""
        device_list = self.find_devices()
        # Exit if no device was found.
        if not device_list:
            print("{}".format(crayons.red("✖  No device matching your configuration was found!")))
            exit(1)
        else:
            print(
                "{} {} {}".format(
                    crayons.green("✔  Found"), len(device_list), crayons.green("devices matching your config.")
                )
            )

        # Downloading the list of products from the server.
        print("{}".format(crayons.blue("➜  Downloading Stock Information for the devices...\n")))

        self.stores_list_with_stock = {}
        for device in minibar.bar(device_list):
            self.check_stores_for_device(device)

        # Get all the stores and sort it by the sequence.
        stores = list(self.stores_list_with_stock.values())
        stores.sort(key=lambda k: k["sequence"])

        # Boolean indicating if the stock is available for any of the items
        # requested (used to play the sound)
        stock_available = False

        # Go through the stores and fetch the stock for all the devices/parts
        # in the store and print their status.
        for store in stores:
            print(
                "\n\n{}, {} ({})".format(
                    crayons.green(store.get("storeName")),
                    crayons.green(store.get("city")),
                    crayons.green(store.get("storeId")),
                )
            )
            for part_id, part in store.get("parts").items():
                if part.get("storeSelectionEnabled") is True:
                    stock_available = True
                    print(
                        " - {} {} ({})".format(
                            crayons.green("✔"),
                            crayons.green(part.get("storePickupProductTitle")),
                            crayons.green(part.get("partNumber")),
                        )
                    )
                else:
                    print(
                        " - {} {} ({})".format(
                            crayons.red("✖"),
                            crayons.red(part.get("storePickupProductTitle")),
                            crayons.red(part.get("partNumber")),
                        )
                    )

        # Play the sound if phone is available.
        if stock_available:
            print("\n{}".format(crayons.green("Current Status - Stock is Available")))
            os.system('say "Device Available!"')
        else:
            print("\n{}".format(crayons.red("Current Status - No Stock Available")))
        print("\n")

        if not not self.configuration.appointment_stores:
            self.get_store_availability()

    def find_devices(self):
        """Find the required devices based on the configuration."""
        # Store the information about the available devices for the family -
        # title, model, carrier.
        device_list = []
        # Downloading the list of products from the server for the current
        # device family.
        print("{}".format(crayons.blue("➜  Downloading Models List...")))
        product_locator_response = requests.get(
            self.PRODUCT_LOCATOR_URL.format(self.base_url, self.configuration.device_family)
        )

        if product_locator_response.status_code != 200 or product_locator_response.json() is None:
            print("----> HERE" + device_list)
            return []

        try:
            product_list = (
                product_locator_response.json()
                .get("body")
                .get("productLocatorOverlayData")
                .get("productLocatorMeta")
                .get("products")
            )
            # Take out the product list and extract only the useful
            # information.
            for product in product_list:
                model = product.get("partNumber")
                carrier = product.get("carrierModel")
                # Only add the requested models and requested carriers (device
                # models are partially matched)
                if (
                    any(item in model for item in self.configuration.selected_device_models)
                    or len(self.configuration.selected_device_models) == 0
                ) and (
                    carrier in self.configuration.selected_carriers or len(self.configuration.selected_carriers) == 0
                ):
                    device_list.append({"title": product.get("productTitle"), "model": model, "carrier": carrier})

        except BaseException:
            print("{}".format(crayons.red("✖  Failed to find the device family")))
            if self.configuration.selected_device_models is not None:
                print("{}".format(crayons.blue("➜  Looking for device models instead...")))
                for model in self.configuration.selected_device_models:
                    device_list.append({"model": model})
        return device_list

    def check_stores_for_device(self, device):
        """Find all stores that have the device requested available (does not matter if it's in stock or not)."""
        product_availability_response = requests.get(
            self.PRODUCT_AVAILABILITY_URL.format(self.base_url, device.get("model"), self.configuration.zip_code)
        )
        store_list = product_availability_response.json().get("body").get("stores")
        # Go through all the stores in the list and extract useful information.
        # Group products by store (put the stock for this device in the store's
        # parts attribute)
        for store in store_list:
            current_store = self.stores_list_with_stock.get(store.get("storeNumber"))
            if current_store is None:
                current_store = {
                    "storeId": store.get("storeNumber"),
                    "storeName": store.get("storeName"),
                    "city": store.get("city"),
                    "sequence": store.get("storeListNumber"),
                    "parts": {},
                }
            new_parts = store.get("partsAvailability")
            old_parts = current_store.get("parts")
            old_parts.update(new_parts)
            current_store["parts"] = old_parts

            # If the store is in the list of user's preferred list, add it to the
            # list to check for stock.
            if (
                store.get("storeNumber") in self.configuration.selected_stores
                or len(self.configuration.selected_stores) == 0
            ):
                self.stores_list_with_stock[store.get("storeNumber")] = current_store

    def get_store_availability(self):
        """Get a list of all the stores to check appointment availability."""
        print("{}".format(crayons.blue("➜  Downloading store appointment availability...\n")))
        store_availability_list = requests.get(
            self.STORE_APPOINTMENT_AVAILABILITY_URL.format(
                datetime.now().strftime("%Y-%m-%d"), datetime.utcnow().strftime("%H")
            )
        )
        slots_found = False
        for store in store_availability_list.json():
            if store.get("storeNumber") in self.configuration.appointment_stores:
                if store.get("appointmentsAvailable") is True:
                    print(
                        " - Appointment Slot Available: {} {} ({})".format(
                            crayons.green("✔"),
                            store.get("storeNumber"),
                            datetime.utcfromtimestamp(int(store.get("firstAvailableAppointment"))).strftime(
                                "%d-%m-%Y %H:%M:%S"
                            ),
                        )
                    )
                    slots_found = True
                else:
                    print(" - {} {}".format(crayons.red("✖"), store.get("storeNumber")))
        if slots_found is True:
            os.system('say "Appointment Slot Available!"')
        print("{}".format(crayons.blue("\n✔  Done\n")))


if __name__ == "__main__":
    store_checker = StoreChecker()
    store_checker.refresh()
