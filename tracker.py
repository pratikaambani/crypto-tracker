import requests
import json
from datetime import datetime
from twitter import *
import sys
import os
import time

while True:
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  consolidated_status = "Hi"
  print(consolidated_status)
  time.sleep(3)
  sys.path.append(".")
