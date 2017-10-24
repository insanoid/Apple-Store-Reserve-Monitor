# Apple Store Reserve Monitor
### Supports iPhone 8 and iPhone X

A simple script to monitor status of the iPhone availability in a given country. Can be changed to any country, device type, and to filter by specific models/carriers/stores. Makes an audio announcement if there is a change in the stock for given configuration. 

### Config.json

The configuration file has the following variables:

1. *country_code* - ISO code for country (2 character) *(required)*
2. *device_family* - `iphone8`, `iphone7`, `iphonex` - should be possible for any other family names. *(required)*
3. *zip_code* - ZIP code to search for (e.g. 90210) *(required)*
4. *models* - List the models you are interested about, it does a partial match so country specific information can be stripped (`MQ8J2LL/A`, `MQ8J2`) default value is all the models.
5. *carriers* - Carriers you are interested in. US carriers - `TMOBILE/US`, `SPRINT/US`, `ATT/US`, `VERIZON/US`, `UNLOCKED/US`. If you are outside US just do not put this in.
6. *stores* - ID of the stores you are interested in (you will have to run the script once to get the store ID), default value is all the stores in that region.

**To get store's ID, and model number, carrier names you will have to run the script once.**

##How To Run:

-  Execute `./storecheck.py` to run once.
-  Execute `./monitor_run_me.py` to keep running it every 30 seconds.

![image](listing.png)
