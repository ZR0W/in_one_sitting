# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:48:36 2023

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
    print(f"chose port number is {PORT}")
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            