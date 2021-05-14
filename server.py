import socket
import threading
import time

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'------------\n[YENİ BAĞLANTI] {addr} |')

def start():
    server.listen()
    print(f'[LISTENING] IP: {SERVER} | PORT: {PORT}')
    time.sleep(2)
    print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f' [ACTIVE CONNECTIONS] {threading.active_count() - 1}')

print("[STARTING]")
time.sleep(1)
start()