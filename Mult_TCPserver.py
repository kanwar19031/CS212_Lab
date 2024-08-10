import socket
import os
from _thread import *
import threading
from datetime import datetime
currentDateAndTime = datetime.now()
ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 43374
ThreadCount = 0
print("Server is ready to bind with client")
# Bind the server socket to the IP and PORT
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)

# A list to keep track of all connected clients
clients = []


def handle_client(client_socket):
    # Continuously receive data from the client and broadcast it to all connected clients
    while True:
        data = client_socket.recv(1024)
        currentTime = currentDateAndTime.strftime("%H:%M:%S")
        print(data.decode('utf_16','strict'), "is in!",currentDateAndTime)
        data2 = client_socket.recv(1024)
        print(data2.decode('utf_16','strict'))
        if not data:
            break
        for client in clients:
            client.send(data2)
    # Remove the client from the list of connected clients
    
# The main server loop
while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    # Add the new client to the list of connected clients
    clients.append(client_socket)

    # Print a message to indicate a new connection
    print(f"connection made with  {client_address}")

    # Start a new thread to handle the new client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    clients.remove(client_socket)
    # Close the client socket
    client_socket.close()
