import requests
import time

# ========= SETTINGS (EDIT ONLY THESE) =========
API_KEY = "a8732f72afd9434d9391361e3b06df79"   # 🔴 PUT YOUR TWELVEDATA API KEY HERE

pairs = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCHF",
        "AUDUSD", "USDCAD", "NZDUSD",
            "EURGBP", "EURJPY", "GBPJPY"
            ]

            # =============================================

            def get_price(symbol):
                try:
                        url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
                                response = requests.get(url)
                                        data = response.json()
                                                return float(data["price"])
                                                    except:
                                                            return None


                                                            def get_signal(price, last_price):
                                                                if last_price is None:
                                                                        return "WAIT"

                                                                            if price > last_price:
                                                                                    return "BUY 📈"
                                                                                        elif price < last_price:
                                                                                                return "SELL 📉"
                                                                                                    else:
                                                                                                            return "HOLD"


                                                                                                            print("🚀 BOT STARTED...\n")

                                                                                                            last_prices = {}

                                                                                                            while True:
                                                                                                                for pair in pairs:
                                                                                                                        price = get_price(pair)

                                                                                                                                if price:
                                                                                                                                            signal = get_signal(price, last_prices.get(pair))
                                                                                                                                                        print(f"{pair} | Price: {price} | Signal: {signal}")

                                                                                                                                                                    last_prices[pair] = price
                                                                                                                                                                            else:
                                                                                                                                                                                        print(f"{pair} | Error getting price")

                                                                                                                                                                                            print("\n🔄 Updating again in 10 seconds...\n")
                                                                                                                                                                                                time.sleep(10)