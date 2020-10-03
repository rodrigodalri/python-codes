'''
author: Rodrigo Dal Ri
email: rodrigodalri1995@gmail.com
'''
import socket

HOST = "127.0.0.1"  
PORT = 8089  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Socket Connected!")
    data = s.recv(1024)

print("Received", repr(data))