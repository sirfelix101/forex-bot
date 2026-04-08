import requests
import time

# ===== CONFIG =====
API_KEY = "a8732f72afd9434d9391361e3b06df79"
TELEGRAM_TOKEN = "8699771655:AAFOydAEDR1vGzW_W8JMqYKlvXxGg7JH218"
CHAT_ID = "159125246"

pairs = ["EURUSD", "GBPUSD"]

# ===== TELEGRAM FUNCTION =====
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
                "chat_id": CHAT_ID,
                        "text": message
                            }
                                requests.post(url, data=data)

                                # ===== GET INDICATORS =====
                                def get_indicator(pair, interval, indicator):
                                    url = f"https://api.twelvedata.com/{indicator}?symbol={pair}&interval={interval}&apikey={API_KEY}"
                                        response = requests.get(url)
                                            data = response.json()
                                                return float(data["values"][0]["value"])

                                                def get_price(pair):
                                                    url = f"https://api.twelvedata.com/price?symbol={pair}&apikey={API_KEY}"
                                                        return float(requests.get(url).json()["price"])

                                                        print("SMART SCALPING BOT STARTED 🚀")

                                                                                 rsi_1m = get_indicator(pair, "1min", "rsi")
                                                                                                                    ema_1m = get_indicator(pair, "1min", "