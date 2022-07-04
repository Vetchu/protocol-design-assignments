from .message import Message
from .message_types import MessageType


class Error(Message):
    def __init__(self, stream_id: int, error_category: int, error_code: int, message):
        super().__init__(stream_id=stream_id, message_type=MessageType.error, seq_number=0x00)
        self.error_category = error_category
        self.error_code = error_code
        self.message = message
