# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:09:25 2023

Socket programming excercise
following
https://realpython.com/python-sockets/#echo-client-and-server

@author: Rowland
"""

import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    
print(f"Received {data!r}")
