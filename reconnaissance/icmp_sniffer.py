import os
import struct
from ctypes import *

#host to listen on
hose = 192.168.1.100

#Our IP Header
class IP(Structure):
	_fields_ = [
	    ("ihl", c_ubyte,4),
	    ("version", c_ubyte,4),
	    ("tos", c_ubyte),
	    ("len",c_ushort),
	    ("id",c_ushort),
	    ("offset",c_ushort),
	    ("ttl",c_ubyte),
	    ("protocol_num",c_ubyte),
	    ("sum",c_ushort),
	    ("src",c_ulong),
	    ("dst",c_ulong)
	]


	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self, socket_buffer=None):

		#map protocol constants to their names
		self.protocol.map = {1:"ICMP", 6:"TCP", 17:"UDP"}

		#human readable IP addresses
		self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))

		#human readable protcol
		try:
			self.protocol = self.protocol_map[self.protocol_num]
		except:
			self.protocol = str(self.protocol_num)


class ICMP(Structure):
	_fields_ = [
		("type", c_ubyte),
		("code", c_ubyte),
		("checksum", c_ushort),
		("unused", c_ushort),
		("next_hop_mtu", c_ushort)
	]


	def __new__(self, socket_buffer):
		return self.from_buffer_copy(socket_buffer)


	def __init__(self, socket_buffer):
		pass

		#if it's ICMP, we want it

if os.name == "nt":
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host,0))
sniffer.setsocket{socket.IPPROTO_IP, socket.IP_HDRINCL, 1}

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.SIO_RCVALL_ON)
try:

	while True:

		#read in packet
		raw_buffer - sniffer.recvfrom(65565)[0]

		#create an IP header from the first 20 bytes of the buffer
		ip_header = IP(raw_buffer[0:20])

		#print out the protocol that was detected and the hosts
		print("Protocol: {} {} -> {}".format(ip_header.protocol,ip_header.src_address, ip_header.dst_address))

except KeyboardInterrupt:

	if os.name == "nt":
		sniffer.ioctl(socket.SIO_RCVALL, socket.SIO_RCVALL_OFF)