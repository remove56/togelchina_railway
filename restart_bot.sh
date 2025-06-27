#!/bin/bash
cd /home/removevj/togelchina_project
pkill -f bot.py
sleep 2
nohup python3.10 bot.py &
