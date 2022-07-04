from .message import Message
from .message_types import MessageType

class ServerHello(Message):
    def __init__(self, stream_id: int, version: int, window_in_messages: int, checksum: int, last_modified: int, file_size_bytes: int):
        super().__init__(stream_id=stream_id, message_type=MessageType.server_hello, seq_number=0x00)
        self.version = version
        self.next_header_type = 0x00
        self.next_header_offset = 0x00
        self.window_in_messages = window_in_messages
        self.checksum = checksum
        self.last_modified = last_modified
        self.file_size_bytes = file_size_bytes
