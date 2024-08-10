
# This is the Server program
#
# Sequence of steps:
#	1. create a "welcome" socket for listening to new connections 
#	2. bind the socket to a host and port
#	3. start listening on this socket for new connections
#	4. accept an incoming connection from the client
#   5. send and receive data over the "connection" socket


import socket

#  create a socket for listening to new connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				# use SOCK_STREAM for TCP
				# use SOCK_DGRAM for UDP

# bind it to a host and a port
host = 'localhost'
port = 43382  # arbitrarily chosen non-privileged port number
s.bind((host,port))
print("Server started...waiting for a connection from the client")

# start listening for TCP connections made to this socket
# the argument "1" is the max number of queued up clients allowed
s.listen(1) 

# accept a connection

connection_socket, addr = s.accept()
print("Connection initiated and adress is:  ",addr)
name = connection_socket.recv(1024)
print("Current user is : ", name.decode('utf_16','strict'))


# receive some bytes and print them
# the argument 1024 is the maximum number of characters to be read at a time
while True:
	data = connection_socket.recv(1024)
	decoded = data.decode('utf_16','strict')
	print("SERVER RECEIVED: ", decoded)

	if decoded == 'q':
		print(name.decode('utf_16','strict'),"left!")
		break
	
	input = decoded.split()

	if input[1] == '+':
		OUT = float(input[0]) + float(input[2])
	elif input[1] == '-':
		OUT = float(input[0]) - float(input[2])
	elif input[1] == '*':
		OUT = float(input[0]) * float(input[2])
	else :
		OUT = float(input[0]) / float(input[2])

	# send some bytes...
	connection_socket.send(str(OUT).encode('utf_16','strict'))
	print("Answer Sent!")

# close the connection
connection_socket.close()

