# Apple Store Reserve Monitor (Now supports iPhone 8 and iPhone X)

A simple script to monitor status of the iPhone availability in a given country. Can be changed to any country and any version of the required device. Makes an audio announcement if there is a change in the stock for the selected store for the selected device. The configuration file has the following variables:

1. country_code - ISO code for country (2 character) (required)
2. device_family - `iphone8` or `iphonex` - should be possible for any other family names. (required)
3. zip_code - ZIP code to search for (e.g. 90210) (required)
4. models - List the models you are interested about. It does a partial match so country specific information can be stripped (`MQ8J2LL/A`, `MQ8J2`)
5. carriers - Carriers you are interested in. US carriers - `TMOBILE/US`, `SPRINT/US`, `ATT/US`, `VERIZON/US`, `UNLOCKED/US`. If you are outside US just do not put this in.
6. stores - ID of the stores you are interested in (you will have to run the script once to get the store ID).

To get store Id, and model, carrier you will have to run the script once.

![image](listing.png)
