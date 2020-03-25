import re
import sys
import time
import os.path
import paramiko

user_file = input("Enter user file name: ")

#Verify the validity of the username/passwd file
if os.path.isfile(user_file) == True:
	
	print("Username/Password file is valid")

else:

	print("File {} does not exist".format(user_file))
	sys.exit()


#Checking commands file
cmd_file = input("Enter commands file name: ")

#Verify the valide cmmands file
if os.path.isfile(cmd_file) == True:

	print("Command file is valid. Sending commands to devices.")

else:

	print("File {} does not exist.".format(cmd_file))
	sys.exit()


#Open SSHv2 connection to the device
def ssh_connection(ip):

	global user_file
	global cmd_file

	#Create SSH connection
	try:

		#Define SSH params
  		selected_user_file = open(user_file, 'r')

  		#Starting from the beginning of the file
  		selected_user_file.seek(0)

  		#Reading username from beginning of the file
  		username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

  		#Start from the beginning of file...grab password
		password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

		#Log into switches
		session = paramiko.SSHClient()

		#Allows auto-accepting unknown host keys
		session.set_missing_host_key_policy(paramiko,AutoAddPolicy())

		#Connect to the device
		session.connect(ip.rstrip("\n"), username=username, password=password)

		#Start an interactive shell session on the router
		connection = session.invoke_shell()

		#Setting terminal length for entire output 
		connection.send("enable\n")
		connection.send("terminal length")
		time.sleep(1)

		#Entering global config mode
		connection.send("\n")
		connection.send("configure terminal")
		time.sleep(1)

		#Open user selected file for reading
		selected_cmd_file = open(cmd_file,'r')

		#Starting from the beginning of the file
		selected_cmd_file.seek(0)