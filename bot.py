import time
import requests

pairs = [
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD",
        "USDCHF", "NZDUSD", "EURGBP", "EURJPY", "GBPJPY"
        ]

def get_price(symbol):
            try:
                    base = symbol[:3]
                            quote = symbol[3:]

                                    url = f"https://api.exchangerate.host/latest?base={base}&symbols={quote}"
                                            response = requests.get(url)
                                                    data = response.json()

                                                            price = data["rates"][quote]
                                                                    return float(price)

                                                                        except:
                                                                                return None


                                                                                print("🚀 BOT STARTED")

                                                                                while True:
                                                                                    for pair in pairs:
                                                                                            price = get_price(pair)

                                                                                                    if price:
                                                                                                                print(f"{pair}: {price}")
                                                                                                                        else:
                                                                                                                                    print(f"{pair}: Error")

                                                                                                                                        print("------")
                                                                                                                                            time.sleep(10)