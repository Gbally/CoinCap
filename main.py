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
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import subprocess
import ConfigParser
import csv

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/05/28'
__copyright__ = ''
__version__ = '0.0.1'
__maintainer__ = 'Guillaume'
__email__ = ''

# [GLOBALS]--------------------------------------------------------------------
DESCRIPTION = """Get data from coinmarketcap"""
PATH = 'Config.rc'
PATTERN = ''

# [Functions]-------------------------------------------------------------------
def main(conf):
    config = ConfigParser.RawConfigParser()
    config.read(conf)
    list_of_coins = config.get('List', 'coins')
    list = list_of_coins.split(",")
    for coin in list:
        print 'Get %s Data' % (coin)
        with open('Output/listing.csv', "rb") as f:
            reader = csv.reader(f)
            for l in enumerate(reader):
                if l[1][0] == coin:
                    try:
                        ID = l[1][2]
                        command = ['python', 'get_data_request.py', ID]
                        cmd = ' '.join(command)
                        output = subprocess.call(cmd, shell=True)
                    except:
                        print "Fail to get ID"

# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
	main(PATH)
