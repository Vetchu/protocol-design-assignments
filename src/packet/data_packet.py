from .base_packet import BasePacket


class DataPacket(BasePacket):
    def __init__(self, packet_type, size, version, seq):
        super().__init__(packet_type, size, version)
        pass
