import sys
import socket
import getopt
import threading
import subprocess

#Define some global variables
listen 				= False
command				= False
upload				= False
execute				= ""
target				= ""
upload_destination  = ""
port				= 0



def usage():

	print "BHP Net Tool"
	print
	print "Usage: bhpnet.py -t target_host -p port"
	print "-l --listen				- listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_run - execute the given file upon receiving a connection"
	print "-c --run_command         - initialize a command shell"
	print "-u --upload=destination  - upon receiving connection upload a file and write to [destination]"





def main():





def client_sender(buffer):




def server_loop():




def run_command(command):



def client_handler():