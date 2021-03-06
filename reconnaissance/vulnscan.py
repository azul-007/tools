#!/usr/bin/python

import socket
import os
import sys

'''Author: Daniel Edwards
Date: 12/21/2019
Description: This program has two functions; retBanner returns the banner information 
from a vulnerable machine. And checkVulns, verifies if the machine is vulnerable via the
banner.'''

#Disclaimer: This script is meant to be used in your own virtual environment against intentionally vulnerable machines.
#Please change the following lines to reflect your environment: 60, 62(range)


#Gets the banner from vuln machine
def retBanner(ip,port):

	try:
		setdefaulttimeout(2)
		sock=socket(ip,port)
		sock.connect((ip,port))
		banner = sock.recv(1024)
		return banner

	except:
		return


#Determines if machine is vulnerable
def checkVulns(banner, filename):
	file = open(filename,'r')
	for line in file.readlines():
		if line.strip('\n') in banner:
			print '[+]Server is vulnerable: ' + banner.strip('\n')


def main():

	if len(sys.argv) == 2:

		filename = sys.argv[1]

		if not os.path.isfile(filename):

			print '[-] File doesn\'t exist'
			exit(0)

		if not os.access(filename, os.R_OK):

			print '[-] Access Denied!'
			exit(0)

	else:

		print '[-] Usage: ' + str(sys.argv[0]) + '<vuln filename>'
		exit(0)

	portlist=[21,23,22,25,80,110,139,443,445]

	for x in range(4,6):
		ip = "192.168.1." + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print '[+] ' + ip + "/" + str(port) + ":" + banner
				checkVulns(banner,filename)

main()
