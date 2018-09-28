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
0.1.3     2018/09/27     Added: Option "Get data from Config file"
0.1.4     2018/09/28     Added Display data from specific coin
						 Menu changed
						 Fixed: Crash if no listing file found
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import sys

from fn_base import pas_tres_class

the_class = pas_tres_class()

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/09/28'
__version__ = '0.1.3'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
PATH = 'Config.rc'

# [Functions]-------------------------------------------------------------------
def main():
	"""
	function: Menu
	return: N/A
	"""
	# For decoration
	head()

	# Set up menu of the script
	menu = {}
	menu['1'] = "Update listing"
	menu['2'] = "Get data from Config file"
	menu['3'] = "Display data from a specific coin"
	menu['4'] = "Exit - Any other key"
	options = menu.keys()
	options.sort()
	for entry in options:
		# Display the menu
		print entry, menu[entry]

	# Save user choice
	user_choice = raw_input("\nChoice [1/%s]: " % len(menu))

	# Update listing is useful for some part of the script to work properly
	# TODO: Out of date date
	if user_choice == "1":
		the_class.get_listing()

		main()

	elif user_choice == "2":
		open("Output/last_update.csv", "w").write("Coin Name," +
		                                          "Price," +
		                                          "Market Cap," +
		                                          "Volume 24h," +
		                                          "change 24h," +
		                                          "change 7 days\n")
		list = the_class.get_data_config_file()
		for coin in list:
			print "\nGet %s data" % coin
			ID = the_class.get_ID_from_listing(coin)
			if not ID:
				main()
			result = the_class.get_coin_data(ID)
			the_class.output_2(result)

		main()

	elif user_choice == "3":
		coin_request = raw_input(
			"Which coin would you like to see? (BTC, LTC, CACH...): ")

		# TODO: Write ID or full coin name - bitcoin - ripple ...
		ID = the_class.get_ID_from_listing(coin_request)
		result = the_class.get_coin_data(ID)
		the_class.output_3(result)

		main()



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
