class Message:
    def __init__(self, stream_id, message_type, seq_number):
        self.stream_id = stream_id
        self.message_type = message_type
        self.seq_number = seq_number
