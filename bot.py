import requests
import time

API_KEY = "a8732f72afd9434d9391361e3b06"

pairs = ["EURUSD","GBPUSD","USDJPY","USDCHF","AUDUSD","USDCAD","NZDUSD","EURGBP","EURJPY","GBPJPY"]

print("BOT STARTED")

while True:
     for pair in pairs:
      try:
        url = "https://api.twelvedata.com/price?symbol=" + pair + "&apikey=" + API_KEY
        response = requests.get(url)
        data = response.json()
        price = float(data["price"])

        print(pair + " | Price: " + str(price))

      except:
                    print(pair + " | Error")

print("------")
time.sleep(10)