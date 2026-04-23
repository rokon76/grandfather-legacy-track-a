import os
import requests

# Use Environment Variables instead of hardcoded strings
TELEGRAM_TOKEN = os.getenv("TG_TOKEN", "YOUR_TOKEN_HERE")
CHAT_ID = os.getenv("TG_CHAT_ID", "YOUR_ID_HERE")

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Alert failed: {e}")
