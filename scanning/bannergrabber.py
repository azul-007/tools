#!/usr/bin/python

from socket import *
from argparse import *

def retBanner(ip,port):

	try:
		setdefaulttimeout(2)
		sock=socket(ip,port)
		sock.connect((ip,port))
		banner = sock.recv(1024)
		return banner

	except:
		return


def main():

	ip = raw_input("Enter target IP: ")

	for port in range(1,1000):

		banner = retBanner(ip,port)

		if banner:

			print "[+]" + ip + str(port) + banner.strip("\n")

main()