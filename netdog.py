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