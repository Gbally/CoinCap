#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : fn_base.py
# DESCRIPTION : In a class, all function that will be used for the project.
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/08/29     Creation of the class
0.1.1     2018/09/27     Added function for "Get data from Config File"
						    - Get data, save and display
0.1.2     2018/09/28     Added function for "Display data from specific coin"
							- Get data and display
						 Fixed: Crash if no listing file found
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import requests
import time
import ConfigParser
import csv
import sys

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/09/28'
__version__ = '0.1.2'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
PATH = 'Config.rc'

# [Functions]-------------------------------------------------------------------
class pas_tres_class:

	def get_coin_data(self, ID):
		"""
		From the URL, add a listing number of the coin to get all the data in
		a JSON format
		"""
		# The request return a json file according to the ID that is added
		# to it - for specific requests
		r = requests.get('https://api.coinmarketcap.com/v2/ticker/' + str(ID))
		return r.json()

	def get_listing(self):
		"""
		The URL gives the listing of every coin referenced in coinmarketcap
		It will be used to get data of every coin
		"""
		# Get the last updated listing list
		print "Updating listing ..."
		r = requests.get('https://api.coinmarketcap.com/v2/listings/')
		self.output_listing(r.json())
		# return r.json()
		return False

	def output_listing(self, data):
		"""
		Write the list of listing in a csv file
		"""
		cpt = 0
		with open("Output/listing.csv", "w") as att_file:
			total_id = len(data["data"]) - 1
			while cpt <= total_id:
				symbol = data["data"][cpt]["symbol"]
				name = data["data"][cpt]["name"]
				id = data["data"][cpt]["id"]
				att_file.write(symbol + "," + name + "," + str(id) + "\n")
				cpt += 1

		print "Update finished and data saved"
		time.sleep(2)
		return False


	def get_data_config_file(self):
		"""
		function: From the config file, launch the get_data_request script.
		return: N/A
		"""
		config = ConfigParser.RawConfigParser()
		config.read(PATH)
		return config.get('List', 'coins').split(",")

	def get_ID_from_listing(self, get_ID):
		"""
		function: Get the ID of the coin requested from the listing.csv file
		return: ID of the coin requested
		"""
		try:
			print "DEBUG: GOOOOOOOOOOD"
			with open('Output/listing.csv', "rb") as f:
				reader = csv.reader(f)
				for l in enumerate(reader):
					if l[1][0] == get_ID:
						return l[1][2]

		except IOError:
			print "Issue with he listing file"
			choice = raw_input(
				"Would you like to update the listing? [y/n]")
			if choice.lower() == "y":
				self.get_listing()
				return False
			else:
				print "Exit script"
				sys.exit(0)

	# def format_request_per_coin(self, data):
	# 	name = data["data"]["name"]
	# 	price = data["data"]["quotes"]["USD"]["price"]
	# 	market_cap = data["data"]["quotes"]["USD"]["market_cap"]
	# 	vol_24 = data["data"]["quotes"]["USD"]["volume_24h"]
	# 	change_24 = data["data"]["quotes"]["USD"]["percent_change_24h"]
	# 	change_7 = data["data"]["quotes"]["USD"]["percent_change_7d"]

	# TODO: Factorize those two functions - possible to merge them
	def output_2(self, result):
		print result
		with open("Output/last_update.csv", "a+") as att_file:
			name = result["data"]["name"]
			price = result["data"]["quotes"]["USD"]["price"]
			market_cap = result["data"]["quotes"]["USD"]["market_cap"]
			vol_24 = result["data"]["quotes"]["USD"]["volume_24h"]
			change_24 = result["data"]["quotes"]["USD"]["percent_change_24h"]
			change_7 = result["data"]["quotes"]["USD"]["percent_change_7d"]

			att_file.write(name + "," + str(price) + "," +
			               str(market_cap) + "," + str(vol_24) + "," +
			               str(change_24) + "," + str(change_7) + "\n")


			#TODO: Print with color for change_24 change_7 | Green + / Red -
			print "\nName : %s" % name
			print "Price : %s" % price
			print "market_cap : %s" % market_cap
			print "Vol_24 : %s" % vol_24
			print "Change_24 : %s" % change_24
			print "Change_7 : %s" % change_7
			time.sleep(1)

	def output_3(self, result):
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

		print '\nName          %s' % name
		print 'Price         %s $' % price
		print 'Market Cap    %s $' % market_cap
		print 'Volume 24h    %s $' % vol_24
		print 'Change 24h    %s /100' % change_24
		print 'Change 7days  %s /100' % change_7