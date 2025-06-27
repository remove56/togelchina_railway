from telegram.ext import Updater, MessageHandler, Filters

def get_chat_id(update, context):
    chat_id = update.effective_chat.id
    print(f"ID grup: {chat_id}")
    update.message.reply_text(f"ID grup ini adalah: {chat_id}")

updater = Updater("7701438631:AAGCLF0AdNZzeDhpyUCTRsTL6HhTqN0u1mk", use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, get_chat_id))
updater.start_polling()
updater.idle()
