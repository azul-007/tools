import socket

target = "127.0.0.1"
target_port = 80

#Create a socket object
client = socket.socket(AF_INET, socket.SOCK_DGRAM)

#Send some data
client.sendto("AAABBBCCC", (target, target_port))

#Receive some data
data, addr = client.recfrom(4096)

print data