import requests

TOKEN = "7701438631:AAGCLF0AdNZzeDhpyUCTRsTL6HhTqN0u1mk"
URL = "https://removevj.pythonanywhere.com/cekid"

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}")
print("STATUS:", r.status_code)
print("RESPONSE:", r.text)
