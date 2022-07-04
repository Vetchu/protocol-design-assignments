from .message import Message
from .message_types import MessageType


class Chunk(Message):
    def __init__(self, stream_id: int, checksum: bytes, payload: bytes):
        super().__init__(stream_id, message_type=MessageType.chunk, seq_number=0x00)
        self.checksum = checksum
        self.payload = payload
