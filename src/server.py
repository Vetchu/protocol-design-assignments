import socket

from utils.consts import MSG_TYPES_REVERSED

SERVER_ADDRESS = ''
SERVER_PORT = 12000


def main(config):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

    while True:
        packet, address = server_socket.recvfrom(1024)

        message_header_type = packet[0]

        message_type = MSG_TYPES_REVERSED[message_header_type]

        print("received", message_type)
        server_socket.sendto(packet, address)
    pass


if __name__ == '__main__':
    main({})
