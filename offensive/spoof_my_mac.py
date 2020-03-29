#!/usr/bin/python3

#Description: This script will change the MAC address of your host
#Author: azul-007

import argparse
import subprocess
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('--interface', '-i', help='Specify an interface')
parser.add_argument('--mac', '-m', help='Specify the MAC Address to change to.')
args = parser.parse_args()

def spoof_mac(interface, mac):

	subprocess.call(["ifconfig",args.interface,"down"])
	subprocess.call(["ifconfig",args.interface,"hw","ether",args.mac])
	subprocess.call(["ifconfig",args.interface,"up"])

	



def main():

	old_mac = subprocess.check_output(["ifconfig",args.interface])
	spoof_mac(interface,mac)
	new_mac = subprocess.check_output(["ifconfig",args.interface])

	if old_mac == new_mac:
		print(colored("[!!] Failed to change MAC to {}".format(args.mac),"red"))
	else:
		print(colored("[+] MAC address changed to: {}".format(args.mac),"green"))

	