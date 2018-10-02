#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : CoinCap.py
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
0.2.0     2018/10/02     Added: Option "Top 10 changes ..."
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import sys

from fn_base import PasTresClass

the_class = PasTresClass()

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/09/28'
__version__ = '0.1.3'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
THIS_FILE = os.path.abspath(os.path.dirname(__file__))
# TODO: To test THIS_FILE
PATH = 'Config.rc'

# [Functions]-------------------------------------------------------------------
def main():
	"""
	function: Menu
	"""
	# For decoration
	head()

	# Set up menu of the script
	print "Update listing --------------------- 1"
	print "Get data from Config file ---------- 2"
	print "Display data from a specific coin -- 3"
	print "Top 10 changes ... ----------------- 4\n"
	print "Exit - Any other key"

	# Save user choice
	user_choice = raw_input("\nChoice [1/4]: ")

	# Update listing is useful for some part of the script to work properly
	# TODO: Out of date data
	if user_choice == "1":
		the_class.get_listing()
		# Return to the main  - menu for an other action
		main()

	# Will display and save coins data from the config file
	elif user_choice == "2":
		# Delete all previous data from the file and add headers
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
			# TODO: If return False - listing file had to be created
			if not ID:
				# And return to main - return to the flow would be better
				main()
			result = the_class.get_coin_data(ID)
			the_class.output_2(result)
		# Return to the main  - menu for an other action
		main()

	elif user_choice == "3":
		coin_request = raw_input(
			"Which coin would you like to see? (BTC, LTC, CACH...): ")

		# TODO: Write ID or full coin name - bitcoin - ripple ...
		ID = the_class.get_ID_from_listing(coin_request)
		result = the_class.get_coin_data(ID)
		the_class.output_3(result)
		raw_input("Press Enter")

		main()

	elif user_choice == "4":
		head()
		# TODO: Let user choose number of values he wishes to see

		print "What information would you like to see:\n"
		print "Changes in the past 1 hour --- 1"
		print "Changes in the past 24 hours - 2"
		print "Changes in the past 7 days --- 3"
		print "Market Cap ------------------- 4"
		print "Value 24 hours --------------- 5"
		print "Price ------------------------ 6"
		user_choice = raw_input("\nYour chocie: ")

		head()
		print "Getting data...\n"
		all_coin_data = the_class.get_coin_data("")
		if user_choice == "1":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "percent_change_1h")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "percent_change_1h")

		elif user_choice == "2":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "percent_change_24h")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "percent_change_24h")

		elif user_choice == "3":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "percent_change_7d")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "percent_change_7d")

		elif user_choice == "4":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "market_cap")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "market_cap")

		elif user_choice == "5":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "volume_24h")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "volume_24h")

		elif user_choice == "6":
			sort_coin_data = the_class.get_data_top_x(all_coin_data,
			                                         "price")
			the_class.process_data_top_x(all_coin_data,
			                             sort_coin_data,
			                             10,
			                             "price")

		raw_input("\nPress Enter to continue...")
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
