#!/usr/bin/python3

import os
import nmap
import argparse
from multiprocessing import Process

#Usage: python boxscan.py --target victim_ip --name name_of_box
#Author: azul-007
#Description
#Creates directory from name of box. Scans target, creates an nmap, nikto 
#and dirb txt file then stores the files in the directory of box name.

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t',help='Specify victim\'s  IP via --target or -t')
parser.add_argument('--name', '-n', help='Specify victim name via --name or -n')
args = parser.parse_args()

os.makedirs(args.name) 
os.chdir(args.name)
os.makedirs(args.name+'/images')

<<<<<<< HEAD
nm = nmap.PortScanner()
trash = nm.scan(args.target,'80') #suppressing output

#Yea I know all these tools have file output options, I move too quickly sometimes
#and forget which box I'm on. So I use these as a reminder. Feel free to change urs
=======
#Yea I know all these tools have file output options, I move too quickly sometimes
#and forget which box I'm on. So I use these as a extra reminder. Feel free to change urs
>>>>>>> 930213e7d0fa1e247c309dfc0bed59365e7b0d30
def nmap():
    os.system('nmap -sV -sT -O -p- {0} > {1}.nmap.txt'.format(args.target,args.name))

def nikto():
    os.system('nikto -host http://{0} > {1}.nikto.txt'.format(args.target,args.name))

def dirb():
    os.system('dirb http://{0} > {1}.dirb.txt'.format(args.target,args.name))
    
def gobuster():
    os.system('gobuster dir -u http://{0} -w ../../../../../usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {1}.gobuster.txt'.format(args.target,args.name))
    
  
if nm[args.target].has_tcp(80):
    p4 = Process(target=gobuster)
    p4.start()
else:
    print("Web server not available")
    
#if __name__ == '__main__':    
    
    p1 = Process(target=nmap)
    p1.start()
    
    p2 = Process(target=nikto)
    p2.start()
    
    p3 = Process(target=dirb)
    p3.start()
                  
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
print("Done!")
