# Apple Store Reserve Monitor

## Supports all iPhone, iPad, and Apple Watch
#### Including iPhone 11 Pro, iPhone 11, iPad 11 Pro, iPad Air 2019
#### Now also check appointment availability due to COVID-19 store entry restrictions

- A script to monitor status of the iPhone/iPad/Watch availability in a given country.
- Configuration file to filter by country, device type, models number, carriers, and stores.
- Makes an audio announcement if there is a change in the stock for given configuration.

### Configuration (Config.json)

The configuration file has the following variables:

1. _country_code_ - ISO code for country (2 character) _(required)_
2. _device_family_ - Filter the device by the apple device family name. _(required)_

| Device Family Names |
|---------------------|
| iphone11pro |
| iphone11 |
| iphonexr |
| iphone8 |
| ipadpro_11 |
| ipadair2019 |
| ipad_10_2_2019 |
| ipadmini2019 |

3. _zip_code_ - ZIP code to search for (e.g. 90210) _(required)_
4. _models_ - List the models you are interested about, it does a partial match so country specific information can be stripped (`MQ8J2LL/A`, `MQ8J2`). The default value is all available models.
5. _carriers_ - Carriers you are interested in. US carriers - `TMOBILE/US`, `SPRINT/US`, `ATT/US`, `VERIZON/US`, `UNLOCKED/US`. If you are outside US do not put this in.
6. _stores_ - ID of the stores you are interested in (you will have to run the script once to get the store ID), default value is all the stores in that region (also available [here](https://gist.github.com/iF2007/ff127f7722af91c47c0cb44d6c1e961d).)
7. appointment_stores -  ID of the stores you want to look for appointments in. This is optional, if you do not put this configuration the app will not look for appointments. In COVID-19 times appointments have become a hassle to get (at least in Berlin).

**To get store's ID, model number, and carrier names you will have to run the script once.**

### Apple Watch

To monitor Apple Watch skip family name parameter and just enter the particular model number. An example configuration would be.

```
{
  "country_code": "us",
  "zip_code": "90210",
  "models": ["MU642LL/A"],
  "stores": ["R462"],
  "appointment_stores": ["R462"],
}
```

You can get the correct model number for the device you are looking for from the URL such as
`https://www.apple.com/shop/buy-watch/apple-watch/silver-aluminum-white-sport-band?preSelect=false&product=MU642LL/A&step=detail#`
the `product` value is the model number, here are a few examples:

- Apple Watch Space Gray Aluminum Case with Sport Band (MWT52LL/A)
- Apple Watch Gold Stainless Steel Case with Sport Loop (MWQN2LL/A)

Thanks to [@rovingrob](https://twitter.com/rovingrob) for pointing this out!

### How To Run:

- Ensure you have Python 3.6 and run `pip install -r requirements.txt`.
- Execute `./store_checker.py` to run once.
- Execute `./monitor.py` to keep running it every 30 seconds.

![image](listing.png)
![image](appointment_slot.png)

### Model Numbers (US)

- These are some model numbers but others can be found easily at third party sellers.
- Keep in mind these are country specific but you can truncate the information to skip the country information.
- To get the exact model code for your country go to your country equivalent of https://www.apple.com/de/shop/product-locator-meta?family=iphone12mini and get the `partNumber`.

| Family Name | Product Name                                    | Carrier     | Model Number |
|-------------|-------------------------------------------------|-------------|--------------|
| iphone12pro| https://www.theiphonewiki.com/wiki/Models (get model from here and add ZD/A at the end for DE and LL/A for US - see above for different countries)                                                |             |              |
| iphone12mini| (same as above - for both 12 and 12 Mini)                      |             |              |
| iphone11pro | iPhone 11 Pro 64GB Space Gray AT&T              | ATT/US      | MW9C2LL/A    |
|             | iPhone 11 Pro 64GB Silver AT&T                  | ATT/US      | MW9D2LL/A    |
|             | iPhone 11 Pro 64GB Gold AT&T                    | ATT/US      | MW9E2LL/A    |
|             | iPhone 11 Pro 64GB Midnight Green AT&T          | ATT/US      | MW9F2LL/A    |
|             | iPhone 11 Pro 256GB Space Gray AT&T             | ATT/US      | MW9G2LL/A    |
|             | iPhone 11 Pro 256GB Silver AT&T                 | ATT/US      | MW9H2LL/A    |
|             | iPhone 11 Pro 256GB Gold AT&T                   | ATT/US      | MW9J2LL/A    |
|             | iPhone 11 Pro 256GB Midnight Green AT&T         | ATT/US      | MW9K2LL/A    |
|             | iPhone 11 Pro 512GB Space Gray AT&T             | ATT/US      | MW9L2LL/A    |
|             | iPhone 11 Pro 512GB Silver AT&T                 | ATT/US      | MW9M2LL/A    |
|             | iPhone 11 Pro 512GB Gold AT&T                   | ATT/US      | MW9N2LL/A    |
|             | iPhone 11 Pro 512GB Midnight Green AT&T         | ATT/US      | MW9P2LL/A    |
|             | iPhone 11 Pro 64GB Space Gray Sprint            | SPRINT/US   | MWA62LL/A    |
|             | iPhone 11 Pro 64GB Silver Sprint                | SPRINT/US   | MWA72LL/A    |
|             | iPhone 11 Pro 64GB Gold Sprint                  | SPRINT/US   | MWA82LL/A    |
|             | iPhone 11 Pro 64GB Midnight Green Sprint        | SPRINT/US   | MWA92LL/A    |
|             | iPhone 11 Pro 256GB Space Gray Sprint           | SPRINT/US   | MWAA2LL/A    |
|             | iPhone 11 Pro 256GB Silver Sprint               | SPRINT/US   | MWAD2LL/A    |
|             | iPhone 11 Pro 256GB Gold Sprint                 | SPRINT/US   | MWAE2LL/A    |
|             | iPhone 11 Pro 256GB Midnight Green Sprint       | SPRINT/US   | MWAF2LL/A    |
|             | iPhone 11 Pro 512GB Space Gray Sprint           | SPRINT/US   | MWAG2LL/A    |
|             | iPhone 11 Pro 512GB Silver Sprint               | SPRINT/US   | MWAH2LL/A    |
|             | iPhone 11 Pro 512GB Gold Sprint                 | SPRINT/US   | MWAJ2LL/A    |
|             | iPhone 11 Pro 512GB Midnight Green Sprint       | SPRINT/US   | MWAL2LL/A    |
|             | iPhone 11 Pro 64GB Space Gray T-Mobile          | TMOBILE/US  | MW9Q2LL/A    |
|             | iPhone 11 Pro 64GB Silver T-Mobile              | TMOBILE/US  | MW9R2LL/A    |
|             | iPhone 11 Pro 64GB Gold T-Mobile                | TMOBILE/US  | MW9T2LL/A    |
|             | iPhone 11 Pro 64GB Midnight Green T-Mobile      | TMOBILE/US  | MW9U2LL/A    |
|             | iPhone 11 Pro 256GB Space Gray T-Mobile         | TMOBILE/US  | MW9V2LL/A    |
|             | iPhone 11 Pro 256GB Silver T-Mobile             | TMOBILE/US  | MW9W2LL/A    |
|             | iPhone 11 Pro 256GB Gold T-Mobile               | TMOBILE/US  | MW9X2LL/A    |
|             | iPhone 11 Pro 256GB Midnight Green T-Mobile     | TMOBILE/US  | MW9Y2LL/A    |
|             | iPhone 11 Pro 512GB Space Gray T-Mobile         | TMOBILE/US  | MWA12LL/A    |
|             | iPhone 11 Pro 512GB Silver T-Mobile             | TMOBILE/US  | MWA32LL/A    |
|             | iPhone 11 Pro 512GB Gold T-Mobile               | TMOBILE/US  | MWA42LL/A    |
|             | iPhone 11 Pro 512GB Midnight Green T-Mobile     | TMOBILE/US  | MWA52LL/A    |
|             | iPhone 11 Pro 64GB Space Gray Verizon           | VERIZON/US  | MWAM2LL/A    |
|             | iPhone 11 Pro 64GB Silver Verizon               | VERIZON/US  | MWAP2LL/A    |
|             | iPhone 11 Pro 64GB Gold Verizon                 | VERIZON/US  | MWAQ2LL/A    |
|             | iPhone 11 Pro 64GB Midnight Green Verizon       | VERIZON/US  | MWAR2LL/A    |
|             | iPhone 11 Pro 256GB Space Gray Verizon          | VERIZON/US  | MWAT2LL/A    |
|             | iPhone 11 Pro 256GB Silver Verizon              | VERIZON/US  | MWAU2LL/A    |
|             | iPhone 11 Pro 256GB Gold Verizon                | VERIZON/US  | MWAV2LL/A    |
|             | iPhone 11 Pro 256GB Midnight Green Verizon      | VERIZON/US  | MWAW2LL/A    |
|             | iPhone 11 Pro 512GB Space Gray Verizon          | VERIZON/US  | MWAX2LL/A    |
|             | iPhone 11 Pro 512GB Silver Verizon              | VERIZON/US  | MWAY2LL/A    |
|             | iPhone 11 Pro 512GB Gold Verizon                | VERIZON/US  | MWC02LL/A    |
|             | iPhone 11 Pro 512GB Midnight Green Verizon      | VERIZON/US  | MWC12LL/A    |
|             | iPhone 11 Pro 64GB Space Gray                   | UNLOCKED/US | MWCH2LL/A    |
|             | iPhone 11 Pro 64GB Silver                       | UNLOCKED/US | MWCJ2LL/A    |
|             | iPhone 11 Pro 64GB Gold                         | UNLOCKED/US | MWCK2LL/A    |
|             | iPhone 11 Pro 64GB Midnight Green               | UNLOCKED/US | MWCL2LL/A    |
|             | iPhone 11 Pro 256GB Space Gray                  | UNLOCKED/US | MWCM2LL/A    |
|             | iPhone 11 Pro 256GB Silver                      | UNLOCKED/US | MWCN2LL/A    |
|             | iPhone 11 Pro 256GB Gold                        | UNLOCKED/US | MWCP2LL/A    |
|             | iPhone 11 Pro 256GB Midnight Green              | UNLOCKED/US | MWCQ2LL/A    |
|             | iPhone 11 Pro 512GB Space Gray                  | UNLOCKED/US | MWCR2LL/A    |
|             | iPhone 11 Pro 512GB Silver                      | UNLOCKED/US | MWCT2LL/A    |
|             | iPhone 11 Pro 512GB Gold                        | UNLOCKED/US | MWCU2LL/A    |
|             | iPhone 11 Pro 512GB Midnight Green              | UNLOCKED/US | MWCV2LL/A    |
|             | iPhone 11 Pro Max 64GB Space Gray AT&T          | ATT/US      | MWF92LL/A    |
|             | iPhone 11 Pro Max 64GB Silver AT&T              | ATT/US      | MWFA2LL/A    |
|             | iPhone 11 Pro Max 64GB Gold AT&T                | ATT/US      | MWFC2LL/A    |
|             | iPhone 11 Pro Max 64GB Midnight Green AT&T      | ATT/US      | MWFD2LL/A    |
|             | iPhone 11 Pro Max 256GB Space Gray AT&T         | ATT/US      | MWFE2LL/A    |
|             | iPhone 11 Pro Max 256GB Silver AT&T             | ATT/US      | MWFF2LL/A    |
|             | iPhone 11 Pro Max 256GB Gold AT&T               | ATT/US      | MWFG2LL/A    |
|             | iPhone 11 Pro Max 256GB Midnight Green AT&T     | ATT/US      | MWFH2LL/A    |
|             | iPhone 11 Pro Max 512GB Space Gray AT&T         | ATT/US      | MWFJ2LL/A    |
|             | iPhone 11 Pro Max 512GB Silver AT&T             | ATT/US      | MWFK2LL/A    |
|             | iPhone 11 Pro Max 512GB Gold AT&T               | ATT/US      | MWFL2LL/A    |
|             | iPhone 11 Pro Max 512GB Midnight Green AT&T     | ATT/US      | MWFM2LL/A    |
|             | iPhone 11 Pro Max 64GB Space Gray Sprint        | SPRINT/US   | MWG22LL/A    |
|             | iPhone 11 Pro Max 64GB Silver Sprint            | SPRINT/US   | MWG32LL/A    |
|             | iPhone 11 Pro Max 64GB Gold Sprint              | SPRINT/US   | MWG42LL/A    |
|             | iPhone 11 Pro Max 64GB Midnight Green Sprint    | SPRINT/US   | MWG52LL/A    |
|             | iPhone 11 Pro Max 256GB Space Gray Sprint       | SPRINT/US   | MWG62LL/A    |
|             | iPhone 11 Pro Max 256GB Silver Sprint           | SPRINT/US   | MWG72LL/A    |
|             | iPhone 11 Pro Max 256GB Gold Sprint             | SPRINT/US   | MWG82LL/A    |
|             | iPhone 11 Pro Max 256GB Midnight Green Sprint   | SPRINT/US   | MWG92LL/A    |
|             | iPhone 11 Pro Max 512GB Space Gray Sprint       | SPRINT/US   | MWGA2LL/A    |
|             | iPhone 11 Pro Max 512GB Silver Sprint           | SPRINT/US   | MWGC2LL/A    |
|             | iPhone 11 Pro Max 512GB Gold Sprint             | SPRINT/US   | MWGD2LL/A    |
|             | iPhone 11 Pro Max 512GB Midnight Green Sprint   | SPRINT/US   | MWGE2LL/A    |
|             | iPhone 11 Pro Max 64GB Space Gray T-Mobile      | TMOBILE/US  | MWFN2LL/A    |
|             | iPhone 11 Pro Max 64GB Silver T-Mobile          | TMOBILE/US  | MWFP2LL/A    |
|             | iPhone 11 Pro Max 64GB Gold T-Mobile            | TMOBILE/US  | MWFQ2LL/A    |
|             | iPhone 11 Pro Max 64GB Midnight Green T-Mobile  | TMOBILE/US  | MWFR2LL/A    |
|             | iPhone 11 Pro Max 256GB Space Gray T-Mobile     | TMOBILE/US  | MWFT2LL/A    |
|             | iPhone 11 Pro Max 256GB Silver T-Mobile         | TMOBILE/US  | MWFU2LL/A    |
|             | iPhone 11 Pro Max 256GB Gold T-Mobile           | TMOBILE/US  | MWFV2LL/A    |
|             | iPhone 11 Pro Max 256GB Midnight Green T-Mobile | TMOBILE/US  | MWFW2LL/A    |
|             | iPhone 11 Pro Max 512GB Space Gray T-Mobile     | TMOBILE/US  | MWFX2LL/A    |
|             | iPhone 11 Pro Max 512GB Silver T-Mobile         | TMOBILE/US  | MWFY2LL/A    |
|             | iPhone 11 Pro Max 512GB Gold T-Mobile           | TMOBILE/US  | MWG02LL/A    |
|             | iPhone 11 Pro Max 512GB Midnight Green T-Mobile | TMOBILE/US  | MWG12LL/A    |
|             | iPhone 11 Pro Max 64GB Space Gray Verizon       | VERIZON/US  | MWGF2LL/A    |
|             | iPhone 11 Pro Max 64GB Silver Verizon           | VERIZON/US  | MWGG2LL/A    |
|             | iPhone 11 Pro Max 64GB Gold Verizon             | VERIZON/US  | MWGH2LL/A    |
|             | iPhone 11 Pro Max 64GB Midnight Green Verizon   | VERIZON/US  | MWGJ2LL/A    |
|             | iPhone 11 Pro Max 256GB Space Gray Verizon      | VERIZON/US  | MWGK2LL/A    |
|             | iPhone 11 Pro Max 256GB Silver Verizon          | VERIZON/US  | MWGL2LL/A    |
|             | iPhone 11 Pro Max 256GB Gold Verizon            | VERIZON/US  | MWGM2LL/A    |
|             | iPhone 11 Pro Max 256GB Midnight Green Verizon  | VERIZON/US  | MWGN2LL/A    |
|             | iPhone 11 Pro Max 512GB Space Gray Verizon      | VERIZON/US  | MWGP2LL/A    |
|             | iPhone 11 Pro Max 512GB Silver Verizon          | VERIZON/US  | MWGQ2LL/A    |
|             | iPhone 11 Pro Max 512GB Gold Verizon            | VERIZON/US  | MWGR2LL/A    |
|             | iPhone 11 Pro Max 512GB Midnight Green Verizon  | VERIZON/US  | MWGT2LL/A    |
|             | iPhone 11 Pro Max 64GB Space Gray               | UNLOCKED/US | MWGY2LL/A    |
|             | iPhone 11 Pro Max 64GB Silver                   | UNLOCKED/US | MWH02LL/A    |
|             | iPhone 11 Pro Max 64GB Gold                     | UNLOCKED/US | MWH12LL/A    |
|             | iPhone 11 Pro Max 64GB Midnight Green           | UNLOCKED/US | MWH22LL/A    |
|             | iPhone 11 Pro Max 256GB Space Gray              | UNLOCKED/US | MWH42LL/A    |
|             | iPhone 11 Pro Max 256GB Silver                  | UNLOCKED/US | MWH52LL/A    |
|             | iPhone 11 Pro Max 256GB Gold                    | UNLOCKED/US | MWH62LL/A    |
|             | iPhone 11 Pro Max 256GB Midnight Green          | UNLOCKED/US | MWH72LL/A    |
|             | iPhone 11 Pro Max 512GB Space Gray              | UNLOCKED/US | MWH82LL/A    |
|             | iPhone 11 Pro Max 512GB Silver                  | UNLOCKED/US | MWH92LL/A    |
|             | iPhone 11 Pro Max 512GB Gold                    | UNLOCKED/US | MWHA2LL/A    |
|             | iPhone 11 Pro Max 512GB Midnight Green          | UNLOCKED/US | MWHC2LL/A    |
| iphone11    | iPhone 11 64GB Black AT&T                       | ATT/US      | MWHT2LL/A    |
|             | iPhone 11 64GB White AT&T                       | ATT/US      | MWHU2LL/A    |
|             | iPhone 11 64GB (PRODUCT)RED AT&T                | ATT/US      | MWHV2LL/A    |
|             | iPhone 11 64GB Yellow AT&T                      | ATT/US      | MWHW2LL/A    |
|             | iPhone 11 64GB Purple AT&T                      | ATT/US      | MWHX2LL/A    |
|             | iPhone 11 64GB Green AT&T                       | ATT/US      | MWHY2LL/A    |
|             | iPhone 11 128GB Black AT&T                      | ATT/US      | MWJ02LL/A    |
|             | iPhone 11 128GB White AT&T                      | ATT/US      | MWJ12LL/A    |
|             | iPhone 11 128GB (PRODUCT)RED AT&T               | ATT/US      | MWJ22LL/A    |
|             | iPhone 11 128GB Yellow AT&T                     | ATT/US      | MWJ32LL/A    |
|             | iPhone 11 128GB Purple AT&T                     | ATT/US      | MWJ42LL/A    |
|             | iPhone 11 128GB Green AT&T                      | ATT/US      | MWJ52LL/A    |
|             | iPhone 11 256GB Black AT&T                      | ATT/US      | MWJ62LL/A    |
|             | iPhone 11 256GB White AT&T                      | ATT/US      | MWJ72LL/A    |
|             | iPhone 11 256GB (PRODUCT)RED AT&T               | ATT/US      | MWJ92LL/A    |
|             | iPhone 11 256GB Yellow AT&T                     | ATT/US      | MWJA2LL/A    |
|             | iPhone 11 256GB Purple AT&T                     | ATT/US      | MWJC2LL/A    |
|             | iPhone 11 256GB Green AT&T                      | ATT/US      | MWJD2LL/A    |
|             | iPhone 11 64GB Black Sprint                     | SPRINT/US   | MWK02LL/A    |
|             | iPhone 11 64GB White Sprint                     | SPRINT/US   | MWK12LL/A    |
|             | iPhone 11 64GB (PRODUCT)RED Sprint              | SPRINT/US   | MWK22LL/A    |
|             | iPhone 11 64GB Yellow Sprint                    | SPRINT/US   | MWK32LL/A    |
|             | iPhone 11 64GB Purple Sprint                    | SPRINT/US   | MWK52LL/A    |
|             | iPhone 11 64GB Green Sprint                     | SPRINT/US   | MWK62LL/A    |
|             | iPhone 11 128GB Black Sprint                    | SPRINT/US   | MWK72LL/A    |
|             | iPhone 11 128GB White Sprint                    | SPRINT/US   | MWK82LL/A    |
|             | iPhone 11 128GB (PRODUCT)RED Sprint             | SPRINT/US   | MWK92LL/A    |
|             | iPhone 11 128GB Yellow Sprint                   | SPRINT/US   | MWKC2LL/A    |
|             | iPhone 11 128GB Purple Sprint                   | SPRINT/US   | MWKD2LL/A    |
|             | iPhone 11 128GB Green Sprint                    | SPRINT/US   | MWKE2LL/A    |
|             | iPhone 11 256GB Black Sprint                    | SPRINT/US   | MWKF2LL/A    |
|             | iPhone 11 256GB White Sprint                    | SPRINT/US   | MWKG2LL/A    |
|             | iPhone 11 256GB (PRODUCT)RED Sprint             | SPRINT/US   | MWKH2LL/A    |
|             | iPhone 11 256GB Yellow Sprint                   | SPRINT/US   | MWKJ2LL/A    |
|             | iPhone 11 256GB Purple Sprint                   | SPRINT/US   | MWKK2LL/A    |
|             | iPhone 11 256GB Green Sprint                    | SPRINT/US   | MWKL2LL/A    |
|             | iPhone 11 64GB Black T-Mobile                   | TMOBILE/US  | MWJE2LL/A    |
|             | iPhone 11 64GB White T-Mobile                   | TMOBILE/US  | MWJF2LL/A    |
|             | iPhone 11 64GB (PRODUCT)RED T-Mobile            | TMOBILE/US  | MWJG2LL/A    |
|             | iPhone 11 64GB Yellow T-Mobile                  | TMOBILE/US  | MWJH2LL/A    |
|             | iPhone 11 64GB Purple T-Mobile                  | TMOBILE/US  | MWJJ2LL/A    |
|             | iPhone 11 64GB Green T-Mobile                   | TMOBILE/US  | MWJK2LL/A    |
|             | iPhone 11 128GB Black T-Mobile                  | TMOBILE/US  | MWJL2LL/A    |
|             | iPhone 11 128GB White T-Mobile                  | TMOBILE/US  | MWJM2LL/A    |
|             | iPhone 11 128GB (PRODUCT)RED T-Mobile           | TMOBILE/US  | MWJN2LL/A    |
|             | iPhone 11 128GB Yellow T-Mobile                 | TMOBILE/US  | MWJP2LL/A    |
|             | iPhone 11 128GB Purple T-Mobile                 | TMOBILE/US  | MWJQ2LL/A    |
|             | iPhone 11 128GB Green T-Mobile                  | TMOBILE/US  | MWJR2LL/A    |
|             | iPhone 11 256GB Black T-Mobile                  | TMOBILE/US  | MWJT2LL/A    |
|             | iPhone 11 256GB White T-Mobile                  | TMOBILE/US  | MWJU2LL/A    |
|             | iPhone 11 256GB (PRODUCT)RED T-Mobile           | TMOBILE/US  | MWJV2LL/A    |
|             | iPhone 11 256GB Yellow T-Mobile                 | TMOBILE/US  | MWJW2LL/A    |
|             | iPhone 11 256GB Purple T-Mobile                 | TMOBILE/US  | MWJX2LL/A    |
|             | iPhone 11 256GB Green T-Mobile                  | TMOBILE/US  | MWJY2LL/A    |
|             | iPhone 11 64GB Black Verizon                    | VERIZON/US  | MWKM2LL/A    |
|             | iPhone 11 64GB White Verizon                    | VERIZON/US  | MWKN2LL/A    |
|             | iPhone 11 64GB (PRODUCT)RED Verizon             | VERIZON/US  | MWKP2LL/A    |
|             | iPhone 11 64GB Yellow Verizon                   | VERIZON/US  | MWKQ2LL/A    |
|             | iPhone 11 64GB Purple Verizon                   | VERIZON/US  | MWKR2LL/A    |
|             | iPhone 11 64GB Green Verizon                    | VERIZON/US  | MWKT2LL/A    |
|             | iPhone 11 128GB Black Verizon                   | VERIZON/US  | MWKU2LL/A    |
|             | iPhone 11 128GB White Verizon                   | VERIZON/US  | MWKV2LL/A    |
|             | iPhone 11 128GB (PRODUCT)RED Verizon            | VERIZON/US  | MWKW2LL/A    |
|             | iPhone 11 128GB Yellow Verizon                  | VERIZON/US  | MWKX2LL/A    |
|             | iPhone 11 128GB Purple Verizon                  | VERIZON/US  | MWKY2LL/A    |
|             | iPhone 11 128GB Green Verizon                   | VERIZON/US  | MWL02LL/A    |
|             | iPhone 11 256GB Black Verizon                   | VERIZON/US  | MWL12LL/A    |
|             | iPhone 11 256GB White Verizon                   | VERIZON/US  | MWL22LL/A    |
|             | iPhone 11 256GB (PRODUCT)RED Verizon            | VERIZON/US  | MWL32LL/A    |
|             | iPhone 11 256GB Yellow Verizon                  | VERIZON/US  | MWL42LL/A    |
|             | iPhone 11 256GB Purple Verizon                  | VERIZON/US  | MWL52LL/A    |
|             | iPhone 11 256GB Green Verizon                   | VERIZON/US  | MWL62LL/A    |
|             | iPhone 11 64GB Black                            | UNLOCKED/US | MWL72LL/A    |
|             | iPhone 11 64GB White                            | UNLOCKED/US | MWL82LL/A    |
|             | iPhone 11 64GB (PRODUCT)RED                     | UNLOCKED/US | MWL92LL/A    |
|             | iPhone 11 64GB Yellow                           | UNLOCKED/US | MWLA2LL/A    |
|             | iPhone 11 64GB Purple                           | UNLOCKED/US | MWLC2LL/A    |
|             | iPhone 11 64GB Green                            | UNLOCKED/US | MWLD2LL/A    |
|             | iPhone 11 128GB Black                           | UNLOCKED/US | MWLE2LL/A    |
|             | iPhone 11 128GB White                           | UNLOCKED/US | MWLF2LL/A    |
|             | iPhone 11 128GB (PRODUCT)RED                    | UNLOCKED/US | MWLG2LL/A    |
|             | iPhone 11 128GB Yellow                          | UNLOCKED/US | MWLH2LL/A    |
|             | iPhone 11 128GB Purple                          | UNLOCKED/US | MWLJ2LL/A    |
|             | iPhone 11 128GB Green                           | UNLOCKED/US | MWLK2LL/A    |
|             | iPhone 11 256GB Black                           | UNLOCKED/US | MWLL2LL/A    |
|             | iPhone 11 256GB White                           | UNLOCKED/US | MWLM2LL/A    |
|             | iPhone 11 256GB (PRODUCT)RED                    | UNLOCKED/US | MWLN2LL/A    |
|             | iPhone 11 256GB Yellow                          | UNLOCKED/US | MWLP2LL/A    |
|             | iPhone 11 256GB Purple                          | UNLOCKED/US | MWLQ2LL/A    |
|             | iPhone 11 256GB Green                           | UNLOCKED/US | MWLR2LL/A    |
| iphonexr    | iPhone XR 64GB Black AT&T                       | ATT/US      | MT3K2LL/A    |
|             | iPhone XR 64GB White AT&T                       | ATT/US      | MT3L2LL/A    |
|             | iPhone XR 64GB (PRODUCT)RED AT&T                | ATT/US      | MT3M2LL/A    |
|             | iPhone XR 64GB Yellow AT&T                      | ATT/US      | MT3N2LL/A    |
|             | iPhone XR 64GB Coral AT&T                       | ATT/US      | MT3Q2LL/A    |
|             | iPhone XR 64GB Blue AT&T                        | ATT/US      | MT3R2LL/A    |
|             | iPhone XR 128GB Black AT&T                      | ATT/US      | MT3T2LL/A    |
|             | iPhone XR 128GB White AT&T                      | ATT/US      | MT3U2LL/A    |
|             | iPhone XR 128GB (PRODUCT)RED AT&T               | ATT/US      | MT3V2LL/A    |
|             | iPhone XR 128GB Yellow AT&T                     | ATT/US      | MT3W2LL/A    |
|             | iPhone XR 128GB Coral AT&T                      | ATT/US      | MT3X2LL/A    |
|             | iPhone XR 128GB Blue AT&T                       | ATT/US      | MT3Y2LL/A    |
|             | iPhone XR 64GB Black Sprint                     | SPRINT/US   | MT472LL/A    |
|             | iPhone XR 64GB White Sprint                     | SPRINT/US   | MT482LL/A    |
|             | iPhone XR 64GB (PRODUCT)RED Sprint              | SPRINT/US   | MT492LL/A    |
|             | iPhone XR 64GB Yellow Sprint                    | SPRINT/US   | MT4A2LL/A    |
|             | iPhone XR 64GB Coral Sprint                     | SPRINT/US   | MT4D2LL/A    |
|             | iPhone XR 64GB Blue Sprint                      | SPRINT/US   | MT4F2LL/A    |
|             | iPhone XR 128GB Black Sprint                    | SPRINT/US   | MT4G2LL/A    |
|             | iPhone XR 128GB White Sprint                    | SPRINT/US   | MT4H2LL/A    |
|             | iPhone XR 128GB (PRODUCT)RED Sprint             | SPRINT/US   | MT4J2LL/A    |
|             | iPhone XR 128GB Yellow Sprint                   | SPRINT/US   | MT4L2LL/A    |
|             | iPhone XR 128GB Coral Sprint                    | SPRINT/US   | MT4N2LL/A    |
|             | iPhone XR 128GB Blue Sprint                     | SPRINT/US   | MT4Q2LL/A    |
|             | iPhone XR 64GB Black T-Mobile                   | TMOBILE/US  | MT2E2LL/A    |
|             | iPhone XR 64GB White T-Mobile                   | TMOBILE/US  | MT2F2LL/A    |
|             | iPhone XR 64GB (PRODUCT)RED T-Mobile            | TMOBILE/US  | MT2G2LL/A    |
|             | iPhone XR 64GB Yellow T-Mobile                  | TMOBILE/US  | MT2H2LL/A    |
|             | iPhone XR 64GB Coral T-Mobile                   | TMOBILE/US  | MT2J2LL/A    |
|             | iPhone XR 64GB Blue T-Mobile                    | TMOBILE/US  | MT2K2LL/A    |
|             | iPhone XR 128GB Black T-Mobile                  | TMOBILE/US  | MT2L2LL/A    |
|             | iPhone XR 128GB White T-Mobile                  | TMOBILE/US  | MT2M2LL/A    |
|             | iPhone XR 128GB (PRODUCT)RED T-Mobile           | TMOBILE/US  | MT2N2LL/A    |
|             | iPhone XR 128GB Yellow T-Mobile                 | TMOBILE/US  | MT2P2LL/A    |
|             | iPhone XR 128GB Coral T-Mobile                  | TMOBILE/US  | MT2Q2LL/A    |
|             | iPhone XR 128GB Blue T-Mobile                   | TMOBILE/US  | MT2R2LL/A    |
|             | iPhone XR 64GB Black Verizon                    | VERIZON/US  | MT302LL/A    |
|             | iPhone XR 64GB White Verizon                    | VERIZON/US  | MT312LL/A    |
|             | iPhone XR 64GB (PRODUCT)RED Verizon             | VERIZON/US  | MT322LL/A    |
|             | iPhone XR 64GB Yellow Verizon                   | VERIZON/US  | MT332LL/A    |
|             | iPhone XR 64GB Coral Verizon                    | VERIZON/US  | MT342LL/A    |
|             | iPhone XR 64GB Blue Verizon                     | VERIZON/US  | MT352LL/A    |
|             | iPhone XR 128GB Black Verizon                   | VERIZON/US  | MT362LL/A    |
|             | iPhone XR 128GB White Verizon                   | VERIZON/US  | MT372LL/A    |
|             | iPhone XR 128GB (PRODUCT)RED Verizon            | VERIZON/US  | MT382LL/A    |
|             | iPhone XR 128GB Yellow Verizon                  | VERIZON/US  | MT392LL/A    |
|             | iPhone XR 128GB Coral Verizon                   | VERIZON/US  | MT3A2LL/A    |
|             | iPhone XR 128GB Blue Verizon                    | VERIZON/US  | MT3C2LL/A    |
|             | iPhone XR 64GB Black                            | UNLOCKED/US | MRYR2LL/A    |
|             | iPhone XR 64GB White                            | UNLOCKED/US | MRYT2LL/A    |
|             | iPhone XR 64GB (PRODUCT)RED                     | UNLOCKED/US | MRYU2LL/A    |
|             | iPhone XR 64GB Yellow                           | UNLOCKED/US | MRYV2LL/A    |
|             | iPhone XR 64GB Coral                            | UNLOCKED/US | MRYW2LL/A    |
|             | iPhone XR 64GB Blue                             | UNLOCKED/US | MRYX2LL/A    |
|             | iPhone XR 128GB Black                           | UNLOCKED/US | MRYY2LL/A    |
|             | iPhone XR 128GB White                           | UNLOCKED/US | MT012LL/A    |
|             | iPhone XR 128GB (PRODUCT)RED                    | UNLOCKED/US | MT022LL/A    |
|             | iPhone XR 128GB Yellow                          | UNLOCKED/US | MT042LL/A    |
|             | iPhone XR 128GB Coral                           | UNLOCKED/US | MT072LL/A    |
|             | iPhone XR 128GB Blue                            | UNLOCKED/US | MT092LL/A    |


### Dev Notes

Project uses the following tools to ensure a well formatted code.
However, as of now it does not have pre-commit hooks or a setup file to run the tools.
- Black (`black .`)
- Pycodestyle (`pycodestyle .`)
- Isort (`isort -y`)
