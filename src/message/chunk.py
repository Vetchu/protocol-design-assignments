from .message import Message


class Chunk(Message):
    def __init__(self, stream_id, checksum, payload):
        super().__init__(stream_id, message_type=0x00, seq_number=0x00)
        pass
