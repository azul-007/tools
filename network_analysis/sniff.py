#!/usr/bin/python3

import socket
import os
import sys
import struct
import binascii

#Author: Daniel Edwards



sock_created = False
sniffer_socket = 0


def analyze_ip_header(data_recv):

	ip_hrd = struct.unpack('!6H4s4s',data_recv[:20]) #Go to struct tables to learn the values of 6H4s4s and 6s6sh


def anaylze_ether_header(data_recv):

	ip_bool = False

	eth_hdr  = struct.unpack('!6s6sh', data_recv[:14])
	dest_mac = binascii.hexlify(eth_hdr[0])
	src_mac  = binascii.hexlify(eth_hdr[1])
	proto    = eth_hdr[2] >> 8
	data     = data_recv[14:]

	print("___________________________ETHERNET HEADER________________________________")
	print("Destination MAC: %s:%s:%s:%s:%s:%s" % dest_mac[0:2],dest_mac[2:4],dest_mac[4:6],dest_mac[6:8],dest_mac[8:10],dest_mac[10:12])
	print("Source Mac: %s:%s:%s:%s:%s:%s" % src_mac[0:2],src_mac[2:4],src_mac[4:6],src_mac[6:8],src_mac[8:10],src_mac[10:12])
	print("PROTOCL: %hu" % proto)

	if proto == 0x08:
	    ip_bool = True:

	return data, ip_bool				


def main()

    global sock_created
    global sniffer_socket
    if sock_created == False:

    	sniffer_socket = socket.socket(socket.PR_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    	sock_created = True


    data_recv = sniffer_socket.recv(2048)
    os.system('clear')

    data_recv, ip_bool = anaylzer_ether_header(data_recv)

    if ip_bool:
    	data_recv, tcp_udp = anaylzer_ether_header(data_recv)

    else:
    	return 