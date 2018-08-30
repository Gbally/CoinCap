#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : cron_task.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/05/29     Creation of the script
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import json
import os
import csv
import requests
import argparse
import datetime
import ConfigParser
import pandas as pd
import numpy as np

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/05/29'
__version__ = '0.0.1'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
THIS_FILE = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = THIS_FILE + '/Config.rc'
LISTING_FILE = THIS_FILE + '/Output/listing.csv'
CRON_OUTPUT = THIS_FILE + '/Output/cron_output.csv'
NOW = datetime.datetime.now()

# [Functions]-------------------------------------------------------------------
def get_list_config():
    """
    function: Get the list of coin from the config file
    return: List of coins
    """
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_FILE)
    list_of_coins = config.get('Monitor', 'coins_monitor')
    list = list_of_coins.split(",")
    return list


def request_listing(coin):
    """
    function: Get the ID of the coin requested from the listing.csv file
    return: ID of the coin requested
    """
    with open(LISTING_FILE, "rb") as f:
        reader = csv.reader(f)
        for l in enumerate(reader):
            if l[1][0] == coin:
                ID = l[1][2]
                return ID


def get_coin_data(ID):
	r = requests.get('https://api.coinmarketcap.com/v2/ticker/' + str(ID))
	return r.json()


def output(json_data):
	# with open("Output/cron_update.csv", "a+") as att_file:
    name = json_data["data"]["name"]
    price = json_data["data"]["quotes"]["USD"]["price"]
    #total_supply = json_data["data"]["total_supply"]
    output = str(name), str(price)
    return output


def save(data_extracted, df):
    # time = get_time()
    # formated = time.get('formated')
    data_extracted = list(data_extracted)
    title = str(data_extracted[0])
    value = data_extracted[1]
    #df = pd.DataFrame({'Time': [formated]})
    df[title] = value
    print "Getting data for %s" % (title)


def get_time():
    year = NOW.year
    month = NOW.month
    day = NOW.day
    hour = NOW.hour
    formated = NOW.strftime("%Y-%m-%d %H:00")
    return {'year': year,'month': month,'day': day,'hour': hour,
            'formated': formated}


def main():
    list = get_list_config()

    if list:
        time = get_time()
        formated = time.get('formated')
        df = pd.DataFrame({'A Time': [formated]})

        list_index = ['A Time']
        for coin in list:
            ID = request_listing(coin)
            json_data = get_coin_data(ID)
            data_extracted = output(json_data)
            list_index.append(data_extracted[0])
            save(data_extracted, df)

        if os.path.exists(CRON_OUTPUT):
            df_exist = pd.read_csv(CRON_OUTPUT)
            df_index = df_exist[list_index]
            new_df = df_index.append(df)
            new_df.to_csv(CRON_OUTPUT)

        else:
            df.to_csv(CRON_OUTPUT)


# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
