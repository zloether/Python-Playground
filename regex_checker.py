#!/usr/bin/env python
# regex_checker.py

# modules needed
from sys import argv
import re, argparse
from luhn10 import luhn10

try:
    script, regex_input_file, data_input_file = argv
except:
    print("Usage: This script takes exactly 2 arguments:")
    print("1) New-line delimited list of regex patterns")
    print("2) File for analysis to identify patterns")
    print("If the Regex patterns file is a CSV, only the first item per line is used")
    print("Output is lines of the file that do not match any of the supplied regex patterns")
    exit()

# -----------------------------------------------------------------------------
# pattern matching for credit card numbers
# -----------------------------------------------------------------------------
def checkREGEX(line, list_of_regex):
    for regex in list_of_regex: # for each regex pattern in list_of_regex
        # find all non-overlapping instances of pattern in 'line'
        matches = re.findall(regex, line, re.IGNORECASE)
        if matches: # if there are matches
            return
    print(line) # print the line if there are no regex matches

# -----------------------------------------------------------------------------
# parseFile
# -----------------------------------------------------------------------------
def parseFile(data_file, regex_input_list):

    # open the input data_file
    data = open(data_file, 'r')

    # iterate through file
    for line in data:
        checkREGEX(line.strip(), regex_input_list)

    data.close()

# -----------------------------------------------------------------------------
# parseREGEX
# -----------------------------------------------------------------------------
def parseREGEX(regex_file):

    regex_list = [] # initialize regex_list

    # open the input data_file
    regex_data = open(regex_file, 'r')

    # iterate through file
    for line in regex_data:
        compiled_regex = line.strip().split(',')[0]
        regex_list.append(compiled_regex)

    regex_data.close()
    return regex_list

# -----------------------------------------------------------------------------
# run it
# -----------------------------------------------------------------------------
regex_list = parseREGEX(regex_input_file)
parseFile(data_input_file, regex_list)
