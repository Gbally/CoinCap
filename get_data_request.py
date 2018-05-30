#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : get_data_request.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/05/28     Creation of the script
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import json
import requests
import argparse
import pandas as pd

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/05/28'
__copyright__ = ''
__version__ = '0.0.1'
__maintainer__ = 'Guillaume'

# [Functions]-------------------------------------------------------------------
def get_coin_data(ID):
	r = requests.get('https://api.coinmarketcap.com/v2/ticker/' + str(ID))
	return r.json()


def output(result):
	with open("Output/last_update.csv", "a+") as att_file:

		name = result["data"]["name"]
		price = result["data"]["quotes"]["USD"]["price"]
		market_cap = result["data"]["quotes"]["USD"]["market_cap"]
		vol_24 = result["data"]["quotes"]["USD"]["volume_24h"]
		change_24 = result["data"]["quotes"]["USD"]["percent_change_24h"]
		change_7 = result["data"]["quotes"]["USD"]["percent_change_7d"]

		att_file.write(name + "," + str(price) + "," + str(market_cap) + ","
		+ str(vol_24) + "," + str(change_24) + "," + str(change_7) + "\n")

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
