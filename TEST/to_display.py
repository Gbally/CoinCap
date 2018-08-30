#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : to_display.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.0.1     2018/05/29     Creation of the script
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import json
import requests
import argparse

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/05/29'
__version__ = '0.0.1'
__maintainer__ = 'Guillaume'

# [Functions]-------------------------------------------------------------------
def get_coin_data(ID):
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/' + str(ID))
    return r.json()

def output(result):
    name = result["data"]["name"]
    price = result["data"]["quotes"]["USD"]["price"]
    market_cap = result["data"]["quotes"]["USD"]["market_cap"]
    vol_24 = result["data"]["quotes"]["USD"]["volume_24h"]
    change_24 = result["data"]["quotes"]["USD"]["percent_change_24h"]
    change_7 = result["data"]["quotes"]["USD"]["percent_change_7d"]

    # Well...it works but that is sooooo disgusting
    if len(str(int(market_cap))) > 12:
        a = len(str(int(market_cap))) - 12
        market_cap = str(int(market_cap))[:a] + " Trillion"
    elif len(str(int(market_cap))) > 9:
        b = len(str(int(market_cap))) - 9
        market_cap = str(int(market_cap))[:b] + " Billion"
    elif len(str(int(market_cap))) > 6:
        b = len(str(int(market_cap))) - 6
        market_cap = str(int(market_cap))[:b] + " Million"
    elif len(str(int(market_cap))) > 3:
        b = len(str(int(market_cap))) - 3
        market_cap = str(int(market_cap))[:b] + " Thousand"

    print 'Name          %s' % (name)
    print 'Price         %s $' % (price)
    print 'Market Cap    %s $' % (market_cap)
    print 'Volume 24h    %s $' % (vol_24)
    print 'Change 24h    %s /100' % (change_24)
    print 'Change 7days  %s /100' % (change_7)
    print ""

def main(ID):
	result = get_coin_data(ID)
	if result:
		return output(result)

# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
	parser = argparse.ArgumentParser(
        description='Need to add a Description, don t be laszy')
	parser.add_argument('ID', action="store", help="Configuration file")
	args = parser.parse_args()
	main(args.ID)
