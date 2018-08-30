#!/bin/sh
echo "----------------------------------------" >> /home/guillaume/Telechargements/git/CoinCap/Output/cron_script_error.log
echo "$(date "+%Y-%m-%d %H:%M:%S")" >> /home/guillaume/Telechargements/git/CoinCap/Output/cron_script_error.log

python /home/guillaume/Telechargements/git/CoinCap/cron_task.py 2>> /home/guillaume/Telechargements/git/CoinCap/Output/cron_script_error.log

