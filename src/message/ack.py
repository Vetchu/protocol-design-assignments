from .message import Message
from consts import MSG_TYPES

class ACK(Message):
    def __init__(self, stream_id, seq_number, window_in_messages, ack_number):
        super().__init__(stream_id=stream_id, message_type=MSG_TYPES["ACK"], seq_number=seq_number)
        self.window_in_messages = window_in_messages
        self.ack_number = ack_number
