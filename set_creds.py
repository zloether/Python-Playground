#!/usr/bin/env python
# set_creds.py

import keyring, getpass

# function to set credentials
def __set_creds(ring, user, pwd):
    try:
        keyring.set_password(ring, user, pwd)
    except ValueError: # catch error from wrong keyring password
        print("Incorrect password for encrypted keyring. Try again!")
        __set_creds(ring, user, pwd) # recursion

# collect info from user
ring = raw_input("Enter keyring name: ")
user = raw_input("Enter user name: ")

# get passphrase
prompt = lambda: (getpass.getpass("Enter passphrase: "), getpass.getpass("Retype passphrase: "))
pwd, pwd2 = prompt()

# verify passphrases match
while pwd != pwd2:
    print("Passphrase does not match. Try again.")
    pwd, pwd2 = prompt()

__set_creds(ring, user, pwd)
