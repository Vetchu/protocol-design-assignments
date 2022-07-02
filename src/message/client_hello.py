from .message import Message


class ClientHello(Message):
    def __init__(self, window_in_messages, start_chunk, file_name):
        super().__init__(stream_id=0x00, message_type=0x01, seq_number=0x00)
        self.version = 0x01
        self.next_header_type = 0x00
        self.next_header_offset = 0x00
        self.window_in_messages = window_in_messages
        self.start_chunk = start_chunk
        self.file_name = file_name
