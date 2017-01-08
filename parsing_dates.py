#!/usr/bin/env python
# parsing_dates.py

# import modules
from dateutil import parser
import datetime
from sys import argv

# get arguments
script, data = argv

# 30 days ago
threshold = datetime.datetime.now() + datetime.timedelta(-30)
date = parser.parse(data)

if date > threshold:
    print(str(date) + " is less than 30 days ago")
else:
    print(str(date) + " is more than 30 days ago")
