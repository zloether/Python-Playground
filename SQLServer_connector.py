#!/usr/bin/env python
# SQLServer_connector.py
# updated: January 8, 2017

#------------------------------------------------------------------------------
# pyodbc documentation:
# https://mkleehammer.github.io/pyodbc/

# SYSTEM REQUIREMENTS:
# This script was written for Python 2.x running on a Windows system. It should
# work with Python 3.x as well.
#
# Your system must have a Microsoft ODBC driver installed. This driver comes
# bundled with SQL Server Management Studio
# https://msdn.microsoft.com/en-us/library/mt238290.aspx
#
# This driver can also be downloaded seperately
# https://www.microsoft.com/en-us/download/details.aspx?id=53339
#
# The included links are current as of 1/8/2017
#------------------------------------------------------------------------------

# import modules
import pyodbc, getpass

# get server info
try: # try this for Python 2.x
    server = raw_input("Server name/IP: ")
    port = raw_input("Port number: ")
    user = raw_input("Username: ")
except NameError: # this will work in Python 3.x
    server = input("Server name/IP: ")
    port = input("Port number: ")
    user = input("Username: ")

# get passphrase
pwd = getpass.getpass("Passphrase: ")

# set Microsoft ODBC driver
driver = "DRIVER={SQL Server}"

# create connection string
connection_string = driver + ';SERVER=' + server + ';PORT=' + port + ';UID=' + user + ';PWD='
print("Connection string: " + connection_string + "<redacted>")

# connect to database
print("Connecting to database...")
try:
    conn = pyodbc.connect(connection_string + pwd)
    cursor = conn.cursor()
except pyodbc.Error as e:
    print(e)
    print("Quitting!")
    exit()

# insert the query you want to execute here
query = '''SELECT ... ;'''

# execute query
try:
    cursor.execute(query)
except pyodbc.Error as e:
    print(e)
    print("Quitting!")
    conn.close() # close DB connection
    exit() # exit the script

row = cursor.fetchone() # grab the first row of data from the query result
while row: # iterate through all the rows of data from the query result
    data = "" # initialize the string output of the row
    i = 0 # index
    while i < len(row)-1:
        data = data + str(row[i]) + ", " # add the next field to the string
        i += 1 # iterate the index

    data = data + str(row[i]) # don't forget the last field in the row

    print(data) # print the row
    row = cursor.fetchone() # grab the next row of the query result

# disconnect from database
print("Disconnecting from database")
conn.close()
