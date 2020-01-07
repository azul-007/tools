#!/usr/bin/python

from socket import *
import optparse
from threading import *


def connScann(tgtHost,tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print '[+] %d/tcp Open' % tgtPort
	except:
		print '[-] %d/tcp Closed' % tgtPort

	finally:
		sock.close()


def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)

	except:
		print 'Unknown host %s' %tgtHost

	try:
		tgtname = gethostbyaddress(tgtIP)
		print 'Results for: ' + tgtname[0]	

	except:
		print 'Results for: ' + tgtIP

	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
	    	t = Thread(target = connScann, args=(tgtHost, int(tgtPort)))
	    	t.start()
	

def main():
	parser = optparse.OptionParser("Usage of program: " + "-H <target host> -p <target ports>")
	parser.add_option('-H', dest='tgtHost', type='string', help='specfiy target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specfiy target ports seperated by commas')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')

	if (tgtHost == None) | (tgtPorts[0] == None):

		print parser.usage
		exit(0)

	portScan(tgtHost,tgtPorts)

if __name__=='__main__':
	main()

