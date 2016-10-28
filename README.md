# Apple Store Reserve Monitor

A simple script to monitor status of the iPhone availability in a given country. Can be changed to any country and any version of the required device. Makes an audio announcement if there is a change in the stock for the selected store for the selected device.

Following are some important variables that you might want to change:

1. **storeurl** - Change this to your region, for example `GB/en_GB` for UK. This fetches a list of stores in your region. Note down `storeNumber` for the stores you want to follow and put it in `pref_stores` array.

2. **availurl** - URL for the stock availability check. Change the region and language to your region in the same way as `storeurl`.

3. **pref_stores** - List of stores that you are interested in knowing stock about.

4. **pref_models** - Model number you are interested in knowing the stock about.

![image](listing.png)
