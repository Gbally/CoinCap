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
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import subprocess
import ConfigParser
import csv
import sys
from fn_base import pas_tres_class

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/06/29'
__version__ = '0.0.1'
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
    print "Get data from Config file ---------- 1"
    print "Display data from a specific coin -- 2"
    print ""
    print "Exit ------------------------- Any Key"
    print ""




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
