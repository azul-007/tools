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

	ip_hdr = struct.unpack('!6H4s4s',data_recv[:20]) #Go to struct tables to learn the values of 6H4s4s and 6s6sh
	ver = ip_hdr[0] >> 12 #Grabs the first two bytes, represented by the H in 6H4s4s.
	ihl = (ip_hdr[0] >> 8) & 0x0f #Taking the data from the ip header, without the version.
	tos = ip_hdr[0] & 0x00ff
	tot_len = ip_hdr[1]
	ip_id = ip_hdr[2]
	flags = ip_hdr[3] >> 13
	frag_offset = ip_hdr[3] & 0x1fff
	ip_ttl = ip_hdr[4] >> 8 
	ip_proto - ip_hdr[4] & 0x00ff
	checksum = ip_hdr[5]
	src_address = sock.inet_ntoa(ip_hdr[6])
	dst_address = sock.inet_ntoa(ip_hdr[7])
	data = data_recv[20:] 

	print("___________________________ETHERNET HEADER________________________________")
	print("Version: %hu" %ver)
	print("IHL: %hu" %ihl)
	print("TOS: %hu" %tos)
	print("Length: %hu" %tot_len)
	print("IP ID: %hu" %ip_id)
	print("Offset: %hu" %frag_offset)
	print("TTL: %hu" %ip_ttl)
	print("Protocol: %hu" %ip_proto)
	print("Checksum: %hu" %checksum)
	print("Source IP: %hu" %src_address)
	print("Destination IP: %hu" %dst_address)

	if ip_proto == 6: #number of tcp header
		tcp_udp = "TCP"
	elif ip_proto == 17:
		tcp_udp = "UDP"
	else:
		tcp_udp = "OTHER"

	return data,tcp_udp




def anaylze_ether_header(data_recv):

	ip_bool = False

	eth_hdr  = struct.unpack('!6s6sH', data_recv[:14]) #The first 6s represents the dest mac. The second 6s represents the src dest. The H corresponds to the remaining two bytes which is the protocol being used. 
	dest_mac = binascii.hexlify(eth_hdr[0])
	src_mac  = binascii.hexlify(eth_hdr[1])
	proto    = eth_hdr[2] >> 8
	data     = data_recv[14:]

	print("___________________________ETHERNET HEADER________________________________")
	print("Destination MAC: %s:%s:%s:%s:%s:%s" % dest_mac[0:2],dest_mac[2:4],dest_mac[4:6],dest_mac[6:8],dest_mac[8:10],dest_mac[10:12])
	print("Source Mac: %s:%s:%s:%s:%s:%s" % src_mac[0:2],src_mac[2:4],src_mac[4:6],src_mac[6:8],src_mac[8:10],src_mac[10:12])
	print("PROTOCL: %hu" % proto)

	if proto == 0x08:
	    ip_bool = True

	return data, ip_bool				


def main():

    global sock_created
    global sniffer_socket
    if sock_created == False:

    	sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    	sock_created = True


    data_recv = sniffer_socket.recv(2048)
    os.system('clear')

    data_recv, ip_bool = anaylzer_ether_header(data_recv)

    if ip_bool:
    	data_recv, tcp_udp = anaylzer_ip_header(data_recv)

    else:
    	return 

    if tcp_udp == "TCP":
    	data_recv = analyze_tcp_header(data_recv)

    elif tcp_udp == "UDP":
    	data_recv = analyze_tcp_header(data_recv)


while True:
	main()