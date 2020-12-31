import os
import sys
import time
from datetime import datetime

from twitter import *

from service import CoinService


# Developed by Pratik Ambani
def format_status(response):
    now = datetime.now()
    current_time = "Current time = " + now.strftime("%H:%M:%S") + " IST \n"

    emoji_btc = "₿"
    emoji_eth = "Ξ"

    usdt_inr = "🔸 USDT(INR): " + str(round(response[0]["rate"], 3)) + "\n"
    btc_usd = "🔸 BTC(USD): " + str(round(response[1]["rate"], 3)) + " " + emoji_btc + "\n"
    btc_inr = "🔸 BTC(INR): " + str(round(response[2]["rate"], 3)) + "\n"
    eth_usd = "🔸 ETH(USD): " + str(round(response[3]["rate"], 3)) + " " + emoji_eth + "\n"
    eth_inr = "🔸 ETH(INR): " + str(round(response[4]["rate"], 3)) + "\n"
    ripple_usd = "🔸 Ripple(USD): " + str(round(response[5]["rate"], 3)) + "\n"
    ripple_inr = "🔸 Ripple(INR): " + str(round(response[6]["rate"], 3)) + "\n"

    tags = "#crypto #BTC #eth #wrx #ripple #BITCOIN 🚀" + "\n"
    developed_by = "- by @prageek_ambani"

    consolidated_status = current_time + usdt_inr + btc_usd + btc_inr + eth_usd + eth_inr + ripple_usd + ripple_inr + tags + developed_by
    return consolidated_status


def sleep(hours):
    time.sleep(hours * 60 * 60)  # 2 hours


def run():
    while True:
        coin_api_response = CoinService.coin_api()
        twitter_status = format_status(coin_api_response)
        print("updated status: %s" % twitter_status)
        sys.path.append(".")
        twitter = Twitter(auth=OAuth(os.environ.get("accessToken"), os.environ.get("accessTokenSecret"),
                                     os.environ.get("consumerKey"), os.environ.get("consumerSecret")))
        results = twitter.statuses.update(status=twitter_status)
        print("status updated")
        sleep(2)  # hours
        print("re-executing")


if __name__ == '__main__':
    run()
