from .message import Message


class Error(Message):
    def __init__(self, stream_id, error_category, error_code, message):
        super().__init__(stream_id=stream_id, message_type=0xff, seq_number=0x00)
        self.error_category = error_category
        self.error_code = error_code
        self.message = message
