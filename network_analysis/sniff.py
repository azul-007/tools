#!/usr/bin/python3

import socket
import os
import sys
import struct
import binascii


sock_created = False
sniffer_socket = 0


def anaylzer_ether_header(data_recv):

	ip_bool = False

	eth_hdr  = struct.unpack('!6s6sh', data_recv[:14])
	dest_mac = binascii.hexlify(eth_hdr[0])
	src_mac  = binascii.hexlify(eth_hdr[1])
	proto    = eth_hdr[2] >> 8
	data     = data_recv[14:]


def main()

    global sock_created
    global sniffer_socket
    if sock_created == False:

    	sniffer_socket = socket.socket(socket.PR_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    	sock_created = True