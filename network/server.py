import socket

HEADERSIZE = 10


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(("192.168.1.13" ,6969))
s.listen()

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    MSG = "Welcome to the server!" 
    MSG = f'{len(MSG):<{HEADERSIZE}}'  +MSG
    clientsocket.send(bytes(MSG,"utf-8"))
    