import requests

TOKEN = "7701438631:AAGCLF0AdNZzeDhpyUCTRsTL6HhTqN0u1mk"
URL = "https://removevj.pythonanywhere.com/cekid"  # Ganti jika URL kamu berbeda

set_webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}"
try:
    response = requests.get(set_webhook_url)
    print("✅ Webhook Request Dikirim")
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)
except Exception as e:
    print("❌ Gagal mengatur webhook:", str(e))
