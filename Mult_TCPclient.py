# This is the client program

# Sequence:
#
# 1. Create a socket
# 2. Connect it to the server process. 
#	We need to know the server's hostname and port.
# 3. Send and receive data 

import socket
import os
from _thread import *

# create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# The first argument AF_INET specifies the addressing family (IP addresses)
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service


# connect to the server
host='localhost'
port=43372  # this is the server's port number, which the client needs to know
s.connect((host,port))

name = input("Enter your name")

# send some bytes
s.send(name.encode('utf-16'))

while True:
	msg = input("Enter the Message you want to broadcast:")
	s.send(msg.encode('utf-16'))
	rec = s.recv(1024)
	print("Broadcast Message :",rec.decode('utf_16','strict'))



s.close()