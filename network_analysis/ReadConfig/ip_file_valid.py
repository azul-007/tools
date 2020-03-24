#!/usr/bin/python3

import os.path
import sys

#Checking IP address and content
def ip_file_valid():

	ip_file = input("Enter IP the name: ")

	if os.path.isfile(ip_file) == True:

		print("File is valid")

	else:

		print("File {} does not exist. Please try again".format(ip_file))
		sys.exit()

		#Read selected file
		selected_ip_file = open(ip_file,'r')

		#Read from beginning
		selected_ip_file.seek(0)

		#Read each line
		ip_list = selected_ip_file.readlines()

		selected_ip_file.close()

		return ip_list