from .message import Message
from .message_types import MessageType

class ACK(Message):
    def __init__(self, stream_id: int, seq_number: int, window_in_messages: int, ack_number: int):
        super().__init__(stream_id=stream_id,
                         message_type=MessageType.ack, seq_number=seq_number)
        self.window_in_messages = window_in_messages
        self.ack_number = ack_number
