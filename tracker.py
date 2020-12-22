import requests
import json
from datetime import datetime
from twitter import *
import sys
import os

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

accessToken = os.environ.get("accessToken");
accessTokenSecret = os.environ.get("accessTokenSecret");
consumerKey = os.environ.get("consumerKey");
consumerSecret = os.environ.get("consumerSecret");

print(accessToken)
print(accessTokenSecret)
print(consumerKey)
print(consumerSecret)

usdt_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/USDT/INR?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
usdt_inr_json = usdt_inr_response.json()

btc_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
btc_usd_json = btc_usd_response.json()

btc_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/INR?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
btc_inr_json = btc_inr_response.json()

eth_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/USD?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
eth_usd_json = eth_usd_response.json()

eth_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/INR?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
eth_inr_json = eth_inr_response.json()

ripple_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/USD?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
ripple_usd_json = ripple_usd_response.json()

ripple_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/INR?apikey=09B84A38-4C8C-482C-992B-A158A10744BC")
ripple_inr_json = ripple_inr_response.json()

current_time = "Current time = " + now.strftime("%H:%M:%S") + "\n"
usdt_inr = "1. USDT(INR): " + str(round(usdt_inr_json["rate"], 3)) + "\n"
btc_usd = "2. BTC(USD): " + str(round(btc_usd_json["rate"], 3)) + "\n"
btc_inr = "3. BTC(INR): " + str(round(btc_inr_json["rate"], 3)) + "\n"
eth_usd = "4. ETH(USD): " + str(round(eth_usd_json["rate"], 3)) + "\n"
eth_inr = "5. ETH(INR): " + str(round(eth_inr_json["rate"], 3)) + "\n"
ripple_usd = "6. Ripple(USD): " + str(round(ripple_usd_json["rate"], 3)) + "\n"
ripple_inr = "7. Ripple(INR): " + str(round(ripple_inr_json["rate"], 3)) + "\n"

consolidated_status = current_time + usdt_inr + btc_usd + btc_inr + eth_usd + eth_inr + ripple_usd + ripple_inr
print(consolidated_status)

sys.path.append(".")
twitter = Twitter(auth = OAuth('1341214000059613185-tIYRH2t5VgWej839VGw64Vt0Z731Gz', 'QRrSJrrqd1oFom8bSlfXIwPlLAQUyBK20YpsnwUSEimmd', 'z52mv5cAcWjEm3XC39UBm2Pgt', 'NLp3KBfdRzacyQRXo1GEKUt62dkaOchwICIf8zilgFkWo9UaRu'))

results = twitter.statuses.update(status = consolidated_status)
print("updated status: %s" % consolidated_status)
