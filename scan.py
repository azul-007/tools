import os
import argparse
from multiprocessing import Process

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t',help='Specify victim\'s  IP via --target or -t')
parser.add_argument('--name', '-n', help='Specify victim name via --name or -n')
args = parser.parse_args()


def nmap():
    os.system('nmap -sV -sC -Pn -sS -O {0} > {1}.nmap.txt'.format(args.target,args.name))

def nikto():
    os.system('nikto -host http://{0} > {1}.nikto.txt'.format(args.target,args.name))

def dirb():
    os.system('dirb http://{0} > {1}.dirb.txt'.format(args.target,args.name))
