import os
import argparse
from multiprocessing import Process


#Usage: python scan.py --target victim_ip --name name_of_box


parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t',help='Specify victim\'s  IP via --target or -t')
parser.add_argument('--name', '-n', help='Specify victim name via --name or -n')
args = parser.parse_args()


def nmap():
    os.system('nmap -sV -Pn -sS -O {0} > {1}.nmap.txt'.format(args.target,args.name))

def nikto():
    os.system('nikto -host http://{0} > {1}.nikto.txt'.format(args.target,args.name))

def dirb():
    os.system('dirb http://{0} > {1}.dirb.txt'.format(args.target,args.name))


if __name__ == '__main__':
    p1 = Process(target=nmap)
    p1.start()
    
    p2 = Process(target=nikto)
    p2.start()
    
    p3 = Process(target=dirb)
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
