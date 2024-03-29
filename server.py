import socket
import select
from CuckooHash import CuckooHash
from Blockchain import block
import pickle

from datetime import datetime
now = datetime.now()

HEADER_LENGTH = 10

DISCONNECT = "!DISCONNECT"
REGISTER = "!REGISTER"
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}
topics = {}
publishers = []
table = CuckooHash(100)

print(f'Listening for connections on {IP}:{PORT}...')

def receive_message(client_socket):

    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        



        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:

        
        return False

while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


    for notified_socket in read_sockets:

        if notified_socket == server_socket:

            
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            publishers.append(user)

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        else:
            


            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue

            
            user = clients[notified_socket]

            
            mess = pickle.loads(message['data'])
            print(mess)
            mess.decryptBlock()

            
            

            # mess = message["data"].decode("utf-8")
            # n = len(mess)

            # print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # if mess[0:9] == REGISTER:
            #     topic = mess[9:]
            #     print(f"Registering {user} for topic: {topic}")

            #     if topic in topics:
            #         topics[topic].append(notified_socket)
            #     else:
            #         interestedsockets = [notified_socket]
            #         topics[topic] = interestedsockets
                
            #     print(topics)
            #     continue


            for client_socket in clients:

                # But don't sent it to sender
                if client_socket != notified_socket:

                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        sockets_list.remove(notified_socket)

        del clients[notified_socket]
