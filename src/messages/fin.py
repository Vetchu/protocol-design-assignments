from .message import Message
from .message_types import MessageType

class FIN(Message):
    def __init__(self, stream_id: int, seq_number: int):
        super().__init__(stream_id=stream_id, message_type=MessageType.fin, seq_number=seq_number)
