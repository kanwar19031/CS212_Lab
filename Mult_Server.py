
import socket
import os
from _thread import *
from datetime import datetime
currentDateAndTime = datetime.now()
ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 43378
ThreadCount = 0

ServerSideSocket.bind((host, port))

print('Socket is listening..')

while True:
    ServerSideSocket.listen(5)
    connection_socket, addr = ServerSideSocket.accept()
    print("Connection initiated and adress is:  ",addr)
    name = connection_socket.recv(1024)
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print("Current user is : ", name.decode('utf_16','strict',),currentDateAndTime)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    data = connection_socket.recv(1024)
    response = 'Server message: ' + data.decode('utf_16','strict')
    connection_socket.sendall(str.encode(response))

# def multi_threaded_client(connection):
#     connection.send(str.encode('Server is working:'))
#     while True:
#         data = connection.recv(1024)
#         response = 'Server message: ' + data.decode('utf_16','strict')
#         connection.sendall(str.encode(response))
#     connection.close()


    # Client, address = ServerSideSocket.accept()
    # print('Connected to: ' + address[0] + ':' + str(address[1]))
    # #start_new_thread(multi_threaded_client, (Client, ))
    

ServerSideSocket.close()



