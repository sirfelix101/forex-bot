1  import time
2  import requests
3
4  pairs = [
5      "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD",
6      "USDCHF","NZDUSD","EURGBP","EURJPY","GBPJPY"
7  ]
8
9  def get_price(symbol):
10     try:
11         url = 
f"https://api.twelvedata.com/price?symbol={symbol}&apikey=demo"
12         response = requests.get(url)
13         data = response.json()
14         return float(data["price"])
15     except:
16         return None
17
18 print("BOT STARTED")
19
20 while True:
21     for pair in pairs:
22         price = get_price(pair)
23
24         if price:
25             print(pair + ": " + str(price))
26         else:
27             print(pair + ": Error")
28
29     print("------")
30     time.sleep(10)
                                                                                                                    time.sleep(10)