#!/usr/bin/python3
import os.path

#Checking IP address and content
def ip_file_valid():

    ip_file = input("Enter IP the name: ")

    while(os.path.isfile(ip_file) == False):

        #print("File is valid")
        ip_file = input("{} is invalid. Please try again: \n".format(ip_file))

    else:
        print("{} is valid \n".format(ip_file))
        

    #Read selected file
    selected_ip_file = open(ip_file,'r')

    #Read from beginning
    selected_ip_file.seek(0)

    #Read each line
    ip_list = selected_ip_file.readlines()

    selected_ip_file.close()

    return ip_list