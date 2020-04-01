import sys
import time
import subprocess

#Check IP reachability
def ip_reach(list):

    for ip in list:

        ip = ip.strip("\n")
        
        ping_reply = subprocess.call('ping {} -c 2'.format(ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        #time.sleep(5)
        
        if ping_reply == 0:
            print("\n* {} is reachable\n".format(ip))
            continue
        else:
            print("\n* {} is NOT reachable".format(ip))
            sys.exit()