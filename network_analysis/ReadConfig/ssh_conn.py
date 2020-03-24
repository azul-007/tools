import os
import sys

user_file = input("Enter user file name: ")

#Verify the validity of the username/passwd file
if os.path.isfile(user_file) == True:
	
	print("Username/Password file is valid")

else:

	print("File {} does not exist".format(user_file))
	sys.exit()