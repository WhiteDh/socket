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
