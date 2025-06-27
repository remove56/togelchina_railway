import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import get_hasil, get_prediksi

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYAIR_LIST = [
    "Langit mendung angka pun turun, malam ini jitu datang di angka 7",
    "Bunga mekar di pagi hari, angka hoki di 83 takkan lari",
    "Ular merayap naik ke dahan, siang malam angka 45 jadi andalan",
    "Mata elang tajam melihat, 29 hadir jadi pilihan tepat"
]

PASARAN = ["SDY", "SGP", "HK"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Selamat datang di Bot Prediksi Togel!\nGunakan /prediksi, /syair, atau /hasil")

async def prediksi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_prediksi()
    if data:
        angka, tanggal = data[1], data[2]
        pasaran = random.choice(PASARAN)
        await update.message.reply_text(f"🎯 Prediksi {pasaran} Hari Ini ({tanggal}):\n🔢 Angka: {angka}")
    else:
        await update.message.reply_text("Belum ada data prediksi.")

async def syair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    syair = random.choice(SYAIR_LIST)
    await update.message.reply_text(f"📜 Syair Hari Ini:\n\n{syair}")

async def hasil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hasil_data = get_hasil()
    if hasil_data:
        angka, tanggal = hasil_data[0][1], hasil_data[0][2]
        pasaran = random.choice(PASARAN)
        await update.message.reply_text(f"📈 Hasil {pasaran} Terbaru ({tanggal}):\n🎰 Angka Keluaran: {angka}")
    else:
        await update.message.reply_text("Belum ada hasil keluaran.")

async def main():
    TOKEN = "7701438631:AAFZWjEB-ed3OB1QfweYMHpQHTJcZqUJ0G8"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prediksi", prediksi))
    app.add_handler(CommandHandler("syair", syair))
    app.add_handler(CommandHandler("hasil", hasil))
    app.add_handler(CommandHandler("syair_sdy", lambda u, c: u.message.reply_text("🌊 Syair SDY: Angka 83 datang dari barat")))
    app.add_handler(CommandHandler("syair_sgp", lambda u, c: u.message.reply_text("🌇 Syair SGP: Bintang malam temani 72")))
    app.add_handler(CommandHandler("syair_hk", lambda u, c: u.message.reply_text("🌃 Syair HK: Langkah pasti angka 91")))
    
    logger.info("Bot berjalan...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
