import sys
import subprocess

#Check IP reachability
def ip_reach(list):

	for ip in list:

		ip = ip.strip("\n")

		ping_reply = subprocess.call("ping %s -c 2" % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if ping_reply == 0:
			print("{} is reachable".format(ip))
			continue
		else:
			print("{} is NOT reachable".format(ip))
			sys.exit()