from .message import Message


class FIN(Message):
    def __init__(self, stream_id, seq_number):
        super().__init__(stream_id=stream_id, message_type=0x04, seq_number=seq_number)
