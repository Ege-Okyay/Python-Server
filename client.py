import socket

SERVER = input('IP: ')
PORT = int(input('PORT: '))
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)