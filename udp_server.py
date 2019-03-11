from socket import *

with socket(AF_INET, SOCK_DGRAM) as serverSocket:
    serverSocket.bind(('', 12000))
    message, address = serverSocket.recvfrom(1024)
    print(address[0] + ":" + message.decode())
