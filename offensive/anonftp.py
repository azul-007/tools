#!/usr/bin/python

import ftplib
from colorama import colored

'''
Author: Daniel Edwards
Date: 12/24/2019
Description: SSH & FTP attacks against metasploitable machine
Disclaimer: This script is meant to be used in your own virtual environment against intentionally vulnerable machines.
'''


def anon_login(hostname):

	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
		print("[*]" + hostname + " FTP Anonymous Login Succeeded")
		ftp.quit()
		return True

	except Exception, e:
		print("[-] Login Failed")