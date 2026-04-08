import requests
import time

API_KEY = "9MOFLJLTNWH3OJPU"

def get_price(symbol):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol[:3]}&to_currency={symbol[3:]}&apikey={API_KEY}"
        
            response = requests.get(url)
                data = response.json()
                    
                        try:
                                price = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
                                        return float(price)
                                            except:
                                                    return None

                                                    print("🚀 BOT STARTED")

                                                    while True:
                                                        price = get_price("EURUSD")
                                                            
                                                                if price:
                                                                        print(f"EUR/USD Price: {price}")
                                                                            else:
                                                                                    print("Error fetching price...")
                                                                                        
                                                                                            time.sleep(10)