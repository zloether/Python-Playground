#!/usr/bin/env python
# computer_object.py

# import modules
from dateutil import parser
import ipaddress, socket, sys

# disable python from generating a .pyc file
sys.dont_write_bytecode = True

# Computer class object. Each computer object has the following attributes:
# hostname, IP address, date (optional).
class computer (object):
    def __init__ (self, hostname, ipaddr, date=""):
        self.hostname = hostname.lower()
        self.ipaddr = ipaddress.IPv4Address(unicode(ipaddr, 'utf-8'))
        if date:
            self.date = parser.parse(date)
        else:
            self.date = date

    # Returns the hostname for the computer object
    def getHostname (self):
        return self.hostname

    # Returns the IP address for the computer object
    def getIP (self):
        return self.ipaddr

    # Returns the date for the computer object
    def getDate (self):
        return self.date

    # Returns all attributes as a List
    def getAll (self):
        if self.date:
            return [self.hostname, self.ipaddr, self.date]
        else:
            return [self.hostname, self.ipaddr]

    # Takes another computer object as an argument and returns True if the
    # IP address matches or False if the IP address is different.
    def equals (self, other_computer):
        if self.ipaddr == other_computer.getIP():
            return True
        else:
            return False

    # Returns comma seperated attributes for the computer object
    def toString (self):
        if self.date:
            return str(self.hostname) + "," + str(self.ipaddr) + "," + str(self.date)
        else:
            return str(self.hostname) + "," + str(self.ipaddr)

    # Returns list of attributes as strings for the computer object
    def toList (self):
        if self.date:
            return [str(self.hostname), str(self.ipaddr), str(self.date)]
        else:
            return [str(self.hostname), str(self.ipaddr)]

    # Compares one computer object to another. If the IP addresses do not match,
    # nothing is returned. If the IPs do match, a computer object is returned
    # that has the hostname, IP, and latest date (if available). If the
    # hostnames do not match, DNS is used to determine the hostname.
    def compare (self, other_computer):

        # get the other computer attributes
        otherName = other_computer.getHostname()
        otherIP = other_computer.getIP()
        otherDate = other_computer.getDate()

        # if IPs are different, return nothing
        if not self.ipaddr == otherIP:
            return

        # determinethe more recent date attributes
        if not self.date and not otherDate:
            newer = ""
        elif self.date and not otherDate:
            newer = self.date
        elif not self.date and otherDate:
            newer = otherDate
        elif self.date > otherDate:
            newer = self.date
        else:
            newer = otherDate

        # compare hostnames and perform DNS lookup if different
        if self.hostname == otherName:
            name = self.hostname
        else:
            name = socket.gethostbyaddr(self.hostname)[0].split('.')[0]

        # return a new computer object
        return computer(str(name), str(self.ipaddr), str(newer))
