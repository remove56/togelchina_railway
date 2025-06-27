#!/bin/bash
# Jalankan hanya di PythonAnywhere console

# Buat virtualenv (opsional jika pakai venv)
# python3 -m venv venv
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jalankan bot.py untuk polling bot Telegram
python3 bot.py