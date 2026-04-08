import time
import requests

# 10 forex pairs
pairs = [
    "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD",
        "USDCHF","NZDUSD","EURGBP","EURJPY","GBPJPY"
        ]

        # get price from API
        def get_price(symbol):
            try:
                    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey=demo"
                            response = requests.get(url)
                                    data = response.json()
                                            return float(data["price"])
                                                except:
                                                        return None

                                                        print("BOT STARTED")

                                                        # main loop
                                                        while True:
                                                            for pair in pairs:
                                                                    price = get_price(pair)
                                                                            
                                                                                    if price:
                                                                                                print(pair + ": " + str(price))
                                                                                                        else:
                                                                                                                    print(pair + ": Error")
                                                                                                                        
                                                                                                                            print("------")
                                                                                                                                time.sleep(10)final clean working bot