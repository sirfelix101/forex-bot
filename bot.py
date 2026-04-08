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

                                                        while True:
                                                            for pair in pairs:
                                                                    try:
                                                                                # ===== LOWER TIMEFRAME (1m) =====
                                                                                            price = get_price(pair)
                                                                                                        rsi_1m = get_indicator(pair, "1min", "rsi")
                                                                                                                    ema_1m = get_indicator(pair, "1min", "ema")
                                                                                                                                atr_1m = get_indicator(pair, "1min", "atr")

                                                                                                                                            # ===== HIGHER TIMEFRAME (5m) =====
                                                                                                                                                        ema_5m = get_indicator(pair, "5min", "ema")

                                                                                                                                                                    print(f"{pair} | Price: {price} | RSI: {rsi_1m}")

                                                                                                                                                                                # ===== TREND (5m) =====
                                                                                                                                                                                            if price > ema_5m:
                                                                                                                                                                                                            trend = "BUY"
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                        trend = "SELL"

                                                                                                                                                                                                                                                    # ===== ENTRY (1m) =====
                                                                                                                                                                                                                                                                if rsi_1m > 55 and price > ema_1m and atr_1m > 0.0005:
                                                                                                                                                                                                                                                                                entry = "BUY"
                                                                                                                                                                                                                                                                                            elif rsi_1m < 45 and price < ema_1m and atr_1m > 0.0005:
                                                                                                                                                                                                                                                                                                            entry = "SELL"
                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                        entry = None

                                                                                                                                                                                                                                                                                                                                                    # ===== FINAL CONFIRMATION =====
                                                                                                                                                                                                                                                                                                                                                                if entry and entry == trend:
                                                                                                                                                                                                                                                                                                                                                                                message = f"🔥 {entry} SIGNAL\nPair: {pair}\nPrice: {price}\nRSI: {rsi_1m}"
                                                                                                                                                                                                                                                                                                                                                                                                print(message)
                                                                                                                                                                                                                                                                                                                                                                                                                send_telegram(message)

                                                                                                                                                                                                                                                                                                                                                                                                                        except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                    print(pair, "Error:", e)

                                                                                                                                                                                                                                                                                                                                                                                                                                        print("------")
                                                                                                                                                                                                                                                                                                                                                                                                                                            time.sleep(15)