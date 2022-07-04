import socket
import time

from messages.message_types import MessageType

CLIENT_ADDRESS = ''
CLIENT_PORT = 8000

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12000

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(30.0)
    message = b'\001test'
    addr = (SERVER_ADDRESS, SERVER_PORT)

    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
    except socket.timeout:
        print('REQUEST TIMED OUT')

streams = []


def main(config):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', config["port"]))

    while True:
        packet, address = server_socket.recvfrom(1024)

        message_header_type = packet[0]
        message_type = MessageType(message_header_type)

    pass


if __name__ == '__main__':
    main({"port": 3000})
