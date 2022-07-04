from .message import Message
from consts import MSG_TYPES



class FIN(Message):
    def __init__(self, stream_id, seq_number):
        super().__init__(stream_id=stream_id, message_type=MSG_TYPES["FIN"], seq_number=seq_number)
