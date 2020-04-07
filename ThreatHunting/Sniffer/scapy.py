import sys
import logging
import netifaces
import subprocess
from datetime import datetime

try:
	from scapy.all import *

except ImportError:
	print("Scapy is not installed.")
	sys.exit()

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

#Get interface
net_iface = input("Enter the interface on which to run: ")

#Verify if interface is up


#if interface is up. Need to download and install this tool in ubuntu
def is_interface_up(net_iface):
	addr = netifaces.ifaddresses(net_iface)
	return netifaces.AF_INET in addr
