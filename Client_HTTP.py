# This is the client program

# Sequence:
#
# 1. Create a socket
# 2. Connect it to the server process. 
#	We need to know the server's hostname and port.
# 3. Send and receive data 

import socket

# create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# The first argument should be AF_INET
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service

# connect to the server
host="www.google.com"
port=80  # this is the server's port number, which the client needs to know

s.connect((host,port))

# send an HTTP GET request
s.send( "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n".encode('utf-16','strict'))

# read a response
response = s.recv(4096)
print(response.decode())


# close the connection
s.close()
