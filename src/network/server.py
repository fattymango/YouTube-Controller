
import socket
import select
import json
from YouTubeController.remote import Remote

class Server:
    def __init__(self,
    remote : Remote = None
    ) -> None:
        
        self.HEADER_LENGTH = 10
        self.IP = "192.168.1.14"
        self.PORT = 1234
        self.server_socket = None
        self.sockets_list = []
        self.clients = {}
        self.remote = remote
        self.__setup() 
        
        
    def __setup(self):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind((socket.gethostbyname(socket.gethostname()), self.PORT))

        self.server_socket.listen()
        self.sockets_list.append(self.server_socket)
        print(f'Listening for connections on {socket.gethostbyname(socket.gethostname())}:{self.PORT}...')

    def __receive_compound_message(self,data):
        command,option = int(data[:2]),data[2:]
        print(command,option)
        return command,option


    def receive_message(self,client_socket):
        try:
            
            message_header = client_socket.recv(self.HEADER_LENGTH)

            if not len(message_header):
                return False

            message_length = int(message_header.decode('utf-8').strip())
            data = client_socket.recv(message_length).decode('utf-8')
            
            return {'header': message_header, 'data':data}

        except:
            return False
    
    def check_new_connection(self):
        
        client_socket, client_address = self.server_socket.accept()
        print(client_address)
        user = self.receive_message(client_socket)
        if user is False:
            return False
        if client_socket not in self.sockets_list:
            self.sockets_list.append(client_socket)
        self.clients[client_socket] = user
        print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data']))
        return True

    def get_new_message(self,notified_socket):
        data = json.dumps(self.remote.get_status())
        message = self.receive_message(notified_socket)['data']
        
        print(message[:2])
        if int(message[:2])>7:
            command,option = self.__receive_compound_message(message)
        else :
            command,option = message,None
        notified_socket.send(bytes(data,encoding="utf-8"))
        notified_socket.close()
        print('Closed connection from: {}'.format(self.clients[notified_socket]['data']))        
        self.sockets_list.remove(notified_socket)
        del self.clients[notified_socket]
        return True, command,option

    
        
    def main(self):
        
        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)
            for notified_socket in read_sockets:
                # new connection case
                if notified_socket == self.server_socket:
                    is_new_conn  = self.check_new_connection() 
                    if not is_new_conn : continue
                    
                #message reciever   
                else:
                    is_new_message, message,option = self.get_new_message(notified_socket)
                    if not is_new_message : continue
                    else : yield  message,option
            for notified_socket in exception_sockets:

                self.sockets_list.remove(notified_socket)

                del self.clients[notified_socket]

    def __del__(self):
        self.server_socket.close()

# while True:
#      for message,option in Server().main():pass