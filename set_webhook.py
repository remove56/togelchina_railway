import requests

TOKEN = "7701438631:AAGCLF0AdNZzeDhpyUCTRsTL6HhTqN0u1mk"
URL = "https://removevj.pythonanywhere.com/cekid"

set_webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}"
response = requests.get(set_webhook_url)

# CETAK status dan respon dari Telegram
print("STATUS:", response.status_code)
print("RESPONSE:", response.text)
