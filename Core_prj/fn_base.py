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
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import requests
import time
import ConfigParser
import csv

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/08/29'
__version__ = '0.1.0'
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
		return r.json()

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
		with open('Output/listing.csv', "rb") as f:
			reader = csv.reader(f)
			for l in enumerate(reader):
				if l[1][0] == get_ID:
					return l[1][2]

	def output(self, result):
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
			print ""
			print "Name : %s" % name
			print "Price : %s" % price
			print "market_cap : %s" % market_cap
			print "Vol_24 : %s" % vol_24
			print "Change_24 : %s" % change_24
			print "Change_7 : %s" % change_7
			time.sleep(1)
