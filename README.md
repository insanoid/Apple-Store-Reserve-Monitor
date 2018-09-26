# Apple Store Reserve Monitor

### Supports all iPhones, iPads, and Apple Watch! (Including iPhone XS and XR!)

A simple script to monitor status of the iPhone availability in a given country. Can be changed to any country, device
type, and to filter by specific models/carriers/stores. Makes an audio announcement if there is a change in the stock
for given configuration.

### Config.json

The configuration file has the following variables:

1. _country_code_ - ISO code for country (2 character) _(required)_
2. _device_family_ - `iphone8`, `iphone7`, `iphonex`, `iphonexr`, `iphonexr`, `ipadpro_10_5`, `ipad_9_7_2018` - should be possible for any other family names. _(required)_
3. _zip_code_ - ZIP code to search for (e.g. 90210) _(required)_
4. _models_ - List the models you are interested about, it does a partial match so country specific information can be stripped (`MQ8J2LL/A`, `MQ8J2`) default value is all the models.
5. _carriers_ - Carriers you are interested in. US carriers - `TMOBILE/US`, `SPRINT/US`, `ATT/US`, `VERIZON/US`, `UNLOCKED/US`. If you are outside US just do not put this in.
6. _stores_ - ID of the stores you are interested in (you will have to run the script once to get the store ID), default value is all the stores in that region.

**To get store's ID, and model number, carrier names you will have to run the script once.**

### Apple Watch

To monitor Apple Watch you can skip family name parameter and just enter the particular model number. An example configuration would
be something as follows.

```
{
  "country_code": "us",
  "zip_code": "90210",
  "models": ["MU642LL/A"],
  "stores": ["R462"]
}
```

You can get the correct model number for the device you are looking for from the URL such as
`https://www.apple.com/shop/buy-watch/apple-watch/silver-aluminum-white-sport-band?preSelect=false&product=MU642LL/A&step=detail#`
the `product` value is the model number, here are a few examples:

- Apple Watch : Silver Aluminum Case with White Sport Band (MU642LL/A)
- Apple Watch : Gold Aluminum Case with Pink Sand Sport Band (MU682LL/A)
- Apple Watch : Space Gray Aluminum Case with Black Sport Band (MU662LL/A)

Thanks to [@rovingrob](https://twitter.com/rovingrob) for pointing this out!

### How To Run:

- Ensure you have Python 3.5.4 and run `pip install -r requirements.txt`.
- Execute `./storecheck.py` to run once.
- Execute `./monitor_run_me.py` to keep running it every 30 seconds.

![image](listing.png)

### Model Numbers (US)

These are some model numbers but others can be found easily at third party sellers. Keep in mind these are country
specific but you can truncate the information to skip the country information.

- iPhone XS 256GB Space Gray (MT972LL/A)
- iPhone XS Max 256GB Silver (MT5E2LL/A)
- iPhone XS 256GB Silver (MT982LL/A)
- iPhone XS Max 512GB Gold (MT5J2LL/A)
- iPhone XS 512GB Space Gray (MT9A2LL/A)
- iPhone XS Max 64GB Silver (MT5A2LL/A)
- iPhone XS 512GB Silver (MT9C2LL/A)
- iPhone XS Max 256GB Space Gray (MT5D2LL/A)
- iPhone XS 64GB Space Gray (MT942LL/A)
- iPhone XS Max 64GB Gold (MT5C2LL/A)
- iPhone XS Max 512GB Space Gray (MT5G2LL/A)
- iPhone XS 64GB Silver (MT952LL/A)
- iPhone XS 256GB Gold (MT992LL/A)
- iPhone XS 64GB Gold (MT962LL/A)
- iPhone XS Max 256GB Gold (MT5F2LL/A)
- iPhone XS Max 64GB Space Gray (MT592LL/A)
- iPhone XS 512GB Gold (MT9D2LL/A)
- iPhone XS Max 512GB Silver (MT5H2LL/A)
- iPhone XR 128GB Coral (MT3A2LL/A)
- iPhone XR 256GB Coral (MT3H2LL/A)
- iPhone XR 256GB Black (MT402LL/A)
- iPhone XR 256GB Black (MT2T2LL/A)
- iPhone XR 128GB Blue (MT3Y2LL/A)
- iPhone XR 256GB Black (MT3D2LL/A)
- iPhone XR 128GB Blue (MT2R2LL/A)
- iPhone XR 256GB (PRODUCT)RED (MT3F2LL/A)
- iPhone XR 256GB Yellow (MT2W2LL/A)
- iPhone XR 128GB Black (MT4G2LL/A)
- iPhone XR 128GB Yellow (MT4L2LL/A)
- iPhone XR 128GB Yellow (MT392LL/A)
- iPhone XR 64GB Coral (MT342LL/A)
- iPhone XR 256GB Coral (MT4X2LL/A)
- iPhone XR 64GB Black (MT3K2LL/A)
- iPhone XR 64GB Black (MT472LL/A)
- iPhone XR 256GB Yellow (MT3G2LL/A)
- iPhone XR 256GB (PRODUCT)RED (MT2V2LL/A)
- iPhone XR 64GB (PRODUCT)RED (MT322LL/A)
- iPhone XR 256GB Coral (MT452LL/A)
- iPhone XR 128GB Blue (MT4Q2LL/A)
- iPhone XR 64GB Coral (MT4D2LL/A)
- iPhone XR 64GB White (MT482LL/A)
- iPhone XR 256GB White (MT412LL/A)
- iPhone XR 64GB (PRODUCT)RED (MT3M2LL/A)
- iPhone XR 64GB Blue (MT3R2LL/A)
- iPhone XR 128GB White (MT3U2LL/A)
- iPhone XR 64GB White (MT3L2LL/A)
- iPhone XR 128GB Blue (MT3C2LL/A)
- iPhone XR 128GB Black (MT2L2LL/A)
- iPhone XR 256GB Blue (MT2Y2LL/A)
- iPhone XR 256GB Yellow (MT4W2LL/A)
- iPhone XR 128GB Black (MT362LL/A)
- iPhone XR 128GB White (MT2M2LL/A)
- iPhone XR 128GB Coral (MT4N2LL/A)
- iPhone XR 256GB Blue (MT4Y2LL/A)
- iPhone XR 128GB Black (MT3T2LL/A)
- iPhone XR 128GB Coral (MT3X2LL/A)
- iPhone XR 256GB (PRODUCT)RED (MT4V2LL/A)
- iPhone XR 64GB Blue (MT2K2LL/A)
- iPhone XR 256GB Yellow (MT442LL/A)
- iPhone XR 128GB (PRODUCT)RED (MT382LL/A)
- iPhone XR 128GB (PRODUCT)RED (MT2N2LL/A)
- iPhone XR 128GB (PRODUCT)RED (MT4J2LL/A)
- iPhone XR 256GB Coral (MT2X2LL/A)
- iPhone XR 256GB (PRODUCT)RED (MT422LL/A)
- iPhone XR 64GB Blue (MT4F2LL/A)
- iPhone XR 64GB Yellow (MT4A2LL/A)
- iPhone XR 256GB Blue (MT462LL/A)
- iPhone XR 128GB Yellow (MT2P2LL/A)
- iPhone XR 256GB White (MT3E2LL/A)
- iPhone XR 64GB Yellow (MT3N2LL/A)
- iPhone XR 256GB Black (MT4R2LL/A)
- iPhone XR 64GB Black (MT302LL/A)
- iPhone XR 64GB Yellow (MT332LL/A)
- iPhone XR 64GB Coral (MT3Q2LL/A)
- iPhone XR 64GB White (MT2F2LL/A)
- iPhone XR 128GB White (MT372LL/A)
- iPhone XR 256GB Blue (MT3J2LL/A)
- iPhone XR 128GB Coral (MT2Q2LL/A)
- iPhone XR 64GB (PRODUCT)RED (MT2G2LL/A)
- iPhone XR 256GB White (MT4U2LL/A)
- iPhone XR 128GB White (MT4H2LL/A)
- iPhone XR 64GB Blue (MT352LL/A)
- iPhone XR 64GB (PRODUCT)RED (MT492LL/A)
- iPhone XR 256GB White (MT2U2LL/A)
- iPhone XR 64GB White (MT312LL/A)
- iPhone XR 64GB Black (MT2E2LL/A)
- iPhone XR 64GB Yellow (MT2H2LL/A)
- iPhone XR 128GB (PRODUCT)RED (MT3V2LL/A)
- iPhone XR 128GB Yellow (MT3W2LL/A)
- iPhone XR 64GB Coral (MT2J2LL/A)
