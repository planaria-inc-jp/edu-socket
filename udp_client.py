from socket import *

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
    addr = ("192.168.1.13", 12000)
    message = input("Please input > ")
    clientSocket.sendto(message.encode(), addr)
