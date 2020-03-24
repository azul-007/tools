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