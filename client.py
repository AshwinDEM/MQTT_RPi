import socket
import threading
import errno
import sys
from Blockchain import block
import pickle

HEADER_LENGTH = 10
DISCONNECT = "!DISCONNECT"
IP = "127.0.0.1"
PORT = 1234
publisher = input("Publisher(y/N)")
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_username.encode('utf-8')
publisher = publisher.encode('utf-8')
username_header = f"{len(username) + 1:<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + publisher + username)

def send_message():
    while True:
        message = input()
        if message:

                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)

def receive_message():
    while True:
        try:
            while True:

                username_header = client_socket.recv(HEADER_LENGTH)

                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()


                username_length = int(username_header.decode('utf-8').strip())

                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length)

                mess = pickle.loads(message)


                print(f'{username} >')
                print(mess)
                mess.decryptBlock()

        except IOError as e:
            
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()


            # continue

        # except Exception as e:
        #     print('Reading error: '.format(str(e)))
        #     sys.exit()

def send_publisher():
    while True:
        topic = input("Enter the topic:\n")
        content = input("Enter the content:\n")
        newBlock = block(username, topic, content)

        msg = pickle.dumps(newBlock)

        if msg:
            message_header = f"{len(msg):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + msg)


def publisher():
    threading.Thread(target = send_publisher).start()
    threading.Thread(target = receive_message).start()

def subscriber():
    threading.Thread(target = send_message).start()
    threading.Thread(target = receive_message).start()

def test():
    threading.Thread(target = send_message).start()
    threading.Thread(target = receive_message).start()

# if publisher:
#     publisher()
# else:
#     subscriber()

publisher()