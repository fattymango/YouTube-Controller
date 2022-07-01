
import socket


HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.13", 6969))

full_msg = ''
new_msg = True

while True:
    msg = s.recv(16)
    if new_msg:
        print("new msg length",msg[:HEADERSIZE])
        msglen = int(msg[:HEADERSIZE])
        new_msg = False
    
    full_msg += msg.decode("utf-8")

    if len(full_msg) - HEADERSIZE == msglen:
        print('msg recvd')
        print(full_msg[HEADERSIZE:])
        print(full_msg)
        full_msg = ''
        new_msg = True

