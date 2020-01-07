#!/usr/bin/python3


from urllib.request import urlopen
import hashlib
from termcolor import colored

#Author: Daniel Edwards
#Date: 1/07/2020
#Description: This program is meant to be used in conjunction with hasher.py


sha1 = input("Enter SHA1 hash value: ")
passlist = str(urlopen("https://github.com/azul-007/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(),"utf-8")

for passwd in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(passwd, "utf-8")).hexdigest()
    if hashguess == sha1:
    	print(colored("[+] Password is: " + str(passwd),"green"))

    else:
    	print(colored("[-] Password Incorrect: " + str(passwd),"red"))

print(colored("Password Not Found"),"yellow")