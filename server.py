<<<<<<< HEAD
import socket
from threading import Thread

# create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))
server_socket.listen()

# wait for the first client to connect
client1_socket, client1_address = server_socket.accept()
print(f'Client 1 connected with {client1_address}')

# wait for the second client to connect
client2_socket, client2_address = server_socket.accept()
print(f'Client 2 connected with {client2_address}')

def receive_from_client(client_socket, client_number):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f'Received from client {client_number}: {data}')
            # send data to the other client
            if client_number == 1:
                client2_socket.send(data.encode())
            else:
                client1_socket.send(data.encode())
        except ConnectionResetError:
            break
    client_socket.close()

# start the receive thread for each client
thread1 = Thread(target=receive_from_client, args=(client1_socket, 1))
thread1.start()

thread2 = Thread(target=receive_from_client, args=(client2_socket, 2))
thread2.start()

# wait for the threads to finish
thread1.join()
thread2.join()

# close the client sockets
client1_socket.close()
print(f'Client 1 disconnected with {client1_address}')

client2_socket.close()
print(f'Client 2 disconnected with {client2_address}')
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
from threading import Thread


sock = socket.socket()
sock.bind(('', 25565))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
sock.listen(1)
conn2, addr2 = sock.accept()
print('connected:', addr2)

def get():
    while True:
        data = conn.recv(1024)
        if data:
            conn2.send(data)
            print(data.decode("utf-8"))

def get2():
    while True:
        data = conn2.recv(1024)
        if data:
            conn.send(data)
            print(data.decode("utf-8"))




Thread(target=get).start()
get2()


conn.close()


# import socket
#
# sock = socket.socket()
# sock.bind(('', 25565))
# sock.listen(1)
# conn, addr = sock.accept()
#
# print('connected:', addr)
#
# while True:
#     data = conn.recv(1024)
#     print(data)
#     if not data:
#         break
#     conn.send(data.upper())
#
# conn.close()
>>>>>>> origin/master
