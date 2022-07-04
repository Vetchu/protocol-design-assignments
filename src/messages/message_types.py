from enum import Enum 

class MessageType(Enum):
    chunk = 0x00
    client_hello = 0x01
    server_hello = 0x02
    ack = 0x03
    fin = 0x04
    error = 0xFF
