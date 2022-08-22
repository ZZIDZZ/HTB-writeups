import pwn
import socket
import time

words = "}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~"

host = "159.65.85.171"
port = 30692

for word in words:
    print(word, hex(ord(word)))
    payload = word
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    clientSocket.connect((host,port))
    clientSocket.send("\x22".encode())
    time.sleep(1)
    clientSocket.send("\x06".encode())
    # Send data to server
    time.sleep(1)
    clientSocket.send(payload.encode())
    # Receive data from server
    dataFromServer = clientSocket.recv(4096)
    # Print to the console
    print(dataFromServer.decode().strip())
    print()