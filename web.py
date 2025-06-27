from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bot China Pools Aktif</h1>"

@app.route('/cekid')
def cekid():
    return "Webhook Aktif dan Siap!"
