#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : plot.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/06/01     Creation of the script
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import os
import csv
import ConfigParser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2018/06/01'
__version__ = '0.1.0'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------
THIS_FILE = os.path.abspath(os.path.dirname(__file__))
CRON_OUTPUT = THIS_FILE + '/Output/cron_output.csv'
CONFIG_FILE = THIS_FILE + '/Config.rc'

# [Functions]-------------------------------------------------------------------



def main():
    df = pd.read_csv(CRON_OUTPUT)
    list_column_file = list(df.columns.values)[2:]
    print list_column_file

# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
