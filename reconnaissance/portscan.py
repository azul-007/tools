#!/bin/bash

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = input("Enter host: ")
def portscanner(port):

	if sock.connect_ex((host, port)):
		print("Port %d is closed" % (port), 'red')
	else:
		print("Port %d is open" % (port), 'green')

for port in range(1,100):
	portscanner(port)