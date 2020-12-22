import requests
import json
from datetime import datetime
from twitter import *
import sys
import os
import time

def coinApiKeyPicker():
  print("inside coinApiKeyPicker()")

  if int(datetime.now().strftime("%H")) < 8:
    apikey="09B84A38-4C8C-482C-992B-A158A10744BC"
  elif int(datetime.now().strftime("%H")) > 16:
    apikey="2353814A-819C-4C22-8803-75FE1E8F2850"
  else:
    apikey="31C67320-5F39-499A-87E3-BEFCB3272316"

  print(apikey)
  return apikey


def coin_api_call():
  print("inside coin_api_call()")

  key = coinApiKeyPicker();
  print("key: ", key)

  usdt_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/USDT/INR?apikey=" + key)
  usdt_inr_json = usdt_inr_response.json()

  btc_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=" + key)
  btc_usd_json = btc_usd_response.json()

  btc_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/INR?apikey=" + key)
  btc_inr_json = btc_inr_response.json()

  eth_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/USD?apikey=" + key)
  eth_usd_json = eth_usd_response.json()

  eth_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/INR?apikey=" + key)
  eth_inr_json = eth_inr_response.json()

  ripple_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/USD?apikey=" + key)
  ripple_usd_json = ripple_usd_response.json()

  ripple_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/INR?apikey=" + key)
  ripple_inr_json = ripple_inr_response.json()

  print("All APIs called")
  return usdt_inr_json, btc_usd_json, btc_inr_json, eth_usd_json, eth_inr_json, ripple_usd_json, ripple_inr_json


def final_status():
  now = datetime.now()
  current_time = "Current time = " + now.strftime("%H:%M:%S") + "\n"
  
  coin_api_response = coin_api_call();
  usdt_inr = "1. USDT(INR): " + str(round(coin_api_response[0]["rate"], 3)) + "\n"
  btc_usd = "2. BTC(USD): " + str(round(coin_api_response[1]["rate"], 3)) + "\n"
  btc_inr = "3. BTC(INR): " + str(round(coin_api_response[2]["rate"], 3)) + "\n"
  eth_usd = "4. ETH(USD): " + str(round(coin_api_response[3]["rate"], 3)) + "\n"
  eth_inr = "5. ETH(INR): " + str(round(coin_api_response[4]["rate"], 3)) + "\n"
  ripple_usd = "6. Ripple(USD): " + str(round(coin_api_response[5]["rate"], 3)) + "\n"
  ripple_inr = "7. Ripple(INR): " + str(round(coin_api_response[6]["rate"], 3)) + "\n"
  
  consolidated_status = current_time + usdt_inr + btc_usd + btc_inr + eth_usd + eth_inr + ripple_usd + ripple_inr
  print(consolidated_status)
  return consolidated_status


while True:
  twt_status = final_status()
  sys.path.append(".")
  twitter = Twitter(auth = OAuth(os.environ.get("accessToken"), os.environ.get("accessTokenSecret"), os.environ.get("consumerKey"), os.environ.get("consumerSecret")))
  results = twitter.statuses.update(status = twt_status)
  print("updated status: %s" % twt_status)
  time.sleep(2 * 60) #X minutes
