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
0.1.0     2018/08/29     Creation of the batch script
0.1.1     2018/09/25     Added: Import class
0.1.1     2018/09/27     Added: Option "Get data from Config file"
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import requests
import subprocess
import ConfigParser
import csv
import sys
from fn_base import pas_tres_class

the_class = pas_tres_class()

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/09/25'
__version__ = '0.1.1'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
PATH = 'Config.rc'

# [Functions]-------------------------------------------------------------------
def main():
	"""
	function: Menu
	return: N/A
	"""
	head()
	print "Updqte listing --------------------- 1"
	print "Get data from Config file ---------- 2"
	print "Display data from a specific coin -- 3"
	print ""
	print "Exit ------------------- Any other Key"
	print ""
	user_choice = raw_input("Choice: ")
	if user_choice == "1":
		the_class.get_listing()
		main()

	elif user_choice == "2":
		list = the_class.get_data_config_file()
		for coin in list:
			print "Get %s data" % coin
			ID = the_class.get_ID_from_listing(coin)
			result = the_class.get_coin_data(ID)
			the_class.output(result)

	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		sys.exit(0)


def head():
	"""
	function: For better looking...in my opinon
	return: N/A
	"""
	os.system('cls' if os.name == 'nt' else 'clear')
	print "-----------------------------------------"
	print "-              CoinCapTool              -"
	print "- Data from https://coinmarketcap.com/  -"
	print "-----------------------------------------"
	print ""

# [MAIN]-----------------------------------------------------------------------


if __name__ == '__main__':
	main()
