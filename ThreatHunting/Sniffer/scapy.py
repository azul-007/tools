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
#if interface is up. 
#def is_interface_up(net_iface):
	#addr = netifaces.ifaddresses(net_iface)
	#return netifaces.AF_INET in addr

try:
	subprocess.call(["ifconfig", net_iface, "promisc"], stdout = None, stderr = None, shell = False)
except:
	print("\nFailed to configure interface as promiscuous.\n")
else:
	print("\nInterface {} was set to PROMSIC mode. \n".format(net_iface))


#Get number of packets to sniff.
pkt_to_sniff = input("Enter # of packets to sniff: ")

if int(pkt_to_sniff) != 0:
	print("\nPackets to capture: {} \n".format(pkt_to_sniff))

elif int(pkt_to_sniff) == 0:
	print("Packets will be captured until timeout expires.\n")

time_to_sniff = input("Enter number of seconds to run the capture: \n")

if int(time_to_sniff) != 0:
	print("\n Packets will be captured for {}".format(time_to_sniff))


#Get protocols to sniff.
proto_sniff = input("* Enter the protocol to filter by (arp|bootp|icmp|0 is all): ")


if (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
    print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
    
elif (proto_sniff) == "0":
    print("\nThe program will capture all protocols.\n")

file_name = input("* Please give a name to the log file: ")
 
#Creating the text file (if it doesn't exist) for packet logging and/or opening it for appending
sniffer_log = open(file_name, "a")


def packet_log(packet):

	now = datetime.now()

	#Log packet information
	if proto_sniff = "0":
		print("Time: " + str(now) + "Protocol: ALL" + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file=sniffer_log)
	elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
		print("Time: " + str(now) + "Protocol: " + proto_sniff.upper() + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file=sniffer_log)

print("\n Starting to sniff...")

#Running the processes
if proto_sniff == "0":
	sniff(iface = net_iface, count = int(pkt_to_sniff), timeout = int(time_to_sniff), prn = packet_log)
elif ((proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp")):
	sniff(iface = net_iface, filter = proto_sniff, count = int(pkt_to_sniff), timeout = int(time_to_sniff), prn = packet_log)
else:
	print("\nCould not ID protocol.\n")

print("\nPackets have been logged to {}".format(file_name))

