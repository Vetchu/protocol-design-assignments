from .message import Message
from src.utils.consts import MSG_TYPES


class Chunk(Message):
    def __init__(self, stream_id, checksum, payload):
        super().__init__(stream_id, message_type=MSG_TYPES["CHUNK"], seq_number=0x00)
        pass
