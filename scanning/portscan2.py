from socket import *
import optparse
from threading import *

def main():
	parser = optparse.OptionParser("Usage of program: " + "-h <target host> -p <taget ports>")
	parser.add_option('-h', dest='tgthost', type='string', help='specfiy target host')
	parser.add_option('-p', dest='tgtpost', type='string', help='specfiy target ports seperated by commas')
	(options, args) = parser.parse_args()
	tgtHost = options.tgthost
	tgtports = str(options.tgtports).split(',')

	if (tgthost == None) | (tgtports[0] == None):

		print(parser.usage)
		exit(0)

	portScan(tgthost,tgtports)

