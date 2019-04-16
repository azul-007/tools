import socket

target 		= "www.google.com"
target_port = 80


#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connect the client
client.connect((target, target_port))

#Send some data
client.send("GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.receive(4096)

print response