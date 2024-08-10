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
	# The first argument AF_INET specifies the addressing family (IP addresses)
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service


# connect to the server
host='localhost'
port=43382  # this is the server's port number, which the client needs to know
s.connect((host,port))

name = input("Enter your name")

# send some bytes
s.send(name.encode('utf-16'))

while True:

	n = str(input("Enter the string"))
	s.send(n.encode('utf_16','strict'))		# 5 + 4
	if n == "q":
		print("BYE")
		break
	str2 = n.isspace() 
	if str2 == True:
		continue
	else: 
		print("Warning! Input is not correct")
	# read a response
	response = s.recv(1024)
	print("RECEIVED Answer from Server is : ",response.decode('utf_16','strict'))
	print("Great This is Correct!")

#s.send(name.encode('utf-16'))

# close the connection
s.close()