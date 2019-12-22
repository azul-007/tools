import socket

target 		= "0.0.0.0"
target_port = 8888


#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connect the client
client.connect((target, target_port))

#Send some data
client.send("GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response