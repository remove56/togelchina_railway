# cek_id_webhook.py
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import os

TOKEN = "7701438631:AAGCLF0AdNZzeDhpyUCTRsTL6HhTqN0u1mk"
bot = Bot(token=TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot, None, workers=0)

# Handler untuk balas dan cetak ID
def get_chat_id(update: Update, context):
    chat_id = update.effective_chat.id
    name = update.effective_chat.title or update.effective_chat.full_name
    context.bot.send_message(chat_id=chat_id, text=f"✅ ID chat ini adalah: `{chat_id}`\n📌 Nama: {name}", parse_mode='Markdown')
    print(f"Chat ID terdeteksi: {chat_id} - Nama: {name}")

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_chat_id))

@app.route('/cekid', methods=['POST'])
def webhook_handler():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

@app.route('/')
def index():
    return 'Bot Webhook aktif'

if __name__ == '__main__':
    app.run(port=5000)
