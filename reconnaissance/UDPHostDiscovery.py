import socket
import os

host = "192.168.1.100"

#Create rack socket and bind to public interface
if os.name = "nt":
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP


sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

#Include IP headers in capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#If using Windows send IOCTL to set promiscuous mode
if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.SIO_RCVALL_ON)

print(sniffer.recv(65565))

#If Windows, turn off promiscuous mode
if os.name = "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.SIO_RCVALL_OFF)