#!/usr/bin/python3

import os
import argparse
from time import process_time
from multiprocessing import Process

#Usage: python boxscan.py --target victim_ip --name name_of_box
#Author: azul-007
#Description
#Creates directory from name of box. Scans target, creates an nmap, nikto 
#and gobuster txt file then stores the files in the directory of box name.

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t',help='Specify victim\'s  IP via --target or -t')
parser.add_argument('--name', '-n', help='Specify victim name via --name or -n')
args = parser.parse_args()

os.chdir('/home/dan/GitHub/boxes/')
os.makedirs(args.name)
os.chdir('/home/dan/GitHub/boxes/'+args.name) 
os.makedirs('/home/dan/GitHub/boxes/'+args.name+'/images')
os.chmod(os.getcwd(),0o660)


def nmap():
    os.system('nmap -sS -A -sU --reason -sC {0} > {1}.nmap.txt'.format(args.target,args.name))

def nikto():
    os.system('nikto -host http://{0} > {1}.nikto.txt'.format(args.target,args.name))

#def dirb():
    #os.system('dirb http://{0} > {1}.dirb.txt'.format(args.target,args.name))
    
def gobuster():
    os.system('gobuster dir -u http://{0} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {1}.gobuster.txt'.format(args.target,args.name))
    
    
if __name__ == '__main__':    
    
    p1 = Process(target=nmap)
    p1.start()
    print("Starting nmap...)
    #nmap_start = process_time()
    
    p2 = Process(target=nikto)
    p2.start()
    print("Starting nikto...)
    #nikto_start = process_time()
    
    p3 = Process(target=gobuster)
    p3.start()
    print("Starting gobuster...")
    #gobuster_start = process_time()
    
                  
    p1.join()
    p2.join()
    p3.join()
    
print("Done!")
