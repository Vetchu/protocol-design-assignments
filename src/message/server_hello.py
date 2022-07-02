from .message import Message


class ServerHello(Message):
    def __init__(self, stream_id, version, window_in_messages, checksum, last_modified, file_size_bytes):
        super().__init__(stream_id=stream_id, message_type=0x02, seq_number=0x00)
        self.version = version
        self.next_header_type = 0x00
        self.next_header_offset = 0x00
        self.window_in_messages = window_in_messages
        self.checksum = checksum
        self.last_modified = last_modified
        self.file_size_bytes = file_size_bytes