from .message_types import MessageType

class Message:
    def __init__(self, stream_id: int, message_type: MessageType, seq_number: int):
        self.stream_id = stream_id
        self.message_type = message_type
        self.seq_number = seq_number
