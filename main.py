#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : main.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.0.1     2018/05/28     Creation of the batch script
0.0.2     2018/05/29     Add Menu
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import subprocess
import ConfigParser
import csv
import sys

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/05/28'
__version__ = '0.0.2'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
DESCRIPTION = """Get data from coinmarketcap"""
PATH = 'Config.rc'

# [Functions]-------------------------------------------------------------------
def main():
    """
    function: Menu
    return: N/A
    """
    head()
    print "Get data from Config file ---------- 1"
    print "Display data from a specific coin -- 2"
    print ""
    print "Exit ------------------------- Any Key"
    print ""
    choice = raw_input("Your choice: ")
    if choice == "1":
        get_data_request()
    elif choice == "2":
        head()
        coin_request = raw_input("With coin would you like to see? (BTC, LTC, CACH...): ")
        ID = request_listing(coin_request)
        try:
            command = ['python', 'to_display.py', ID]
            head()
            cmd = ' '.join(command)
            output = subprocess.call(cmd, shell=True)
        except:
            print "Fail to get ID"
        wait = raw_input("Press enter to continue")
        main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

def get_data_request():
    """
    function: From the config file, launch the get_data_request script.
    return: N/A
    """
    head()
    config = ConfigParser.RawConfigParser()
    config.read(PATH)
    list_of_coins = config.get('List', 'coins')
    list = list_of_coins.split(",")
    for coin in list:
        print 'Get %s Data' % (coin)
        ID = request_listing(coin)
        try:
            command = ['python', 'get_data_request.py', ID]
            cmd = ' '.join(command)
            output = subprocess.call(cmd, shell=True)
        except:
            print "Fail to get ID"

def request_listing(get_ID):
    """
    function: Get the ID of the coin requested from the listing.csv file
    return: ID of the coin requested
    """
    with open('Output/listing.csv', "rb") as f:
        reader = csv.reader(f)
        for l in enumerate(reader):
            if l[1][0] == get_ID:
                ID = l[1][2]
                return ID

def head():
    """
    function: For better looking...in my opinon
    return: N/A
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print "---------------------------------"
    print "-          CoinCapTool          -"
    print "---------------------------------"
    print ""

# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
	main()
