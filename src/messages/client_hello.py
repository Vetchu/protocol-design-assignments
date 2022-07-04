from .message import Message
from .message_types import MessageType


class ClientHello(Message):
    def __init__(self, window_in_messages: int, start_chunk: int, file_name: str):
        super().__init__(stream_id=0x00, message_type=MessageType.client_hello, seq_number=0x00)
        self.version = 0x01
        self.next_header_type = 0x00
        self.next_header_offset = 0x00
        self.window_in_messages = window_in_messages
        self.start_chunk = start_chunk
        self.file_name = file_name
