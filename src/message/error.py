from .message import Message
from src.utils.consts import MSG_TYPES


class Error(Message):
    def __init__(self, stream_id, error_category, error_code, message):
        super().__init__(stream_id=stream_id, message_type=MSG_TYPES["ERROR"], seq_number=0x00)
        self.error_category = error_category
        self.error_code = error_code
        self.message = message
