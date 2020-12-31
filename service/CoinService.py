from datetime import datetime

import requests


# Developed by Pratik Ambani

# keys are publicly available
def coin_api_key_picker():
    print("inside coin_api_key_picker()")
    if int(datetime.now().strftime("%H")) < 8:
        apikey = "2353814A-819C-4C22-8803-75FE1E8F2850"
    elif int(datetime.now().strftime("%H")) > 16:
        apikey = "31C67320-5F39-499A-87E3-BEFCB3272316"
    else:
        apikey = "09B84A38-4C8C-482C-992B-A158A10744BC"
    return apikey


def coin_api():
    print("inside coin_api()")

    api_key = coin_api_key_picker()

    usdt_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/USDT/INR?apikey=" + api_key)
    usdt_inr_json = usdt_inr_response.json()
    btc_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=" + api_key)
    btc_usd_json = btc_usd_response.json()
    btc_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/INR?apikey=" + api_key)
    btc_inr_json = btc_inr_response.json()
    eth_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/USD?apikey=" + api_key)
    eth_usd_json = eth_usd_response.json()
    eth_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/INR?apikey=" + api_key)
    eth_inr_json = eth_inr_response.json()
    ripple_usd_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/USD?apikey=" + api_key)
    ripple_usd_json = ripple_usd_response.json()
    ripple_inr_response = requests.get("https://rest.coinapi.io/v1/exchangerate/XRP/INR?apikey=" + api_key)
    ripple_inr_json = ripple_inr_response.json()

    # mock = '{ "time": "2020-12-31T02:29:34.5952364Z", "asset_id_base": "XRP", "asset_id_quote": "INR", "rate": 17.064774711853807777936899055 }'
    # mock_json = json.loads(mock)
    # usdt_inr_json, btc_usd_json, btc_inr_json, eth_usd_json, eth_inr_json, ripple_usd_json, ripple_inr_json = mock_json, mock_json, mock_json, mock_json, mock_json, mock_json, mock_json

    print("All APIs called")
    return usdt_inr_json, btc_usd_json, btc_inr_json, eth_usd_json, eth_inr_json, ripple_usd_json, ripple_inr_json
