# Error conditions and handling them

The protocol handles six types of errors:

- INCORRECT CONNECTION ID (ERR TYPE: 0x00)

The error occurs when the CONNECTION ID field in an INIT PACKET sent by the client contains a number already used for another connection by the server. The server MUST send an error packet in which it MAY include a suggested CONNECTION ID in the payload of the subheader. The error causes an immediate end of the connection.

- INCORRECT VERSION (ERR TYPE: 0x01)

The error occurs when the VERSION field in an INIT PACKET sent by the client contains a version not accepted by the server. The server MUST send an error packet in which it includes a comma-separated list of available versions in the payload of the subheader. The error causes an immediate end of the connection.

- FILE NOT FOUND (ERR TYPE: 0x02)

The error occurs when the FILE ID field in an INIT PACKET sent by the client contains a path to a non-existing file in the downloading mode. The server MUST send an error packet. The error causes an immediate end of the connection.

- FILE EXISTS (ERR TYPE: 0x03)

The error occurs when the FILE ID field in an INIT PACKET sent by the client contains a path to an existing file in the uploading mode. The server MUST send an error packet. The error causes an immediate end of the connection.

- ABORT DOWNLOAD (ERR TYPE: 0x04)

The error is caused by the ABORT DOWNLOAD error packet sent by either client or server. It causes immediate stopping of downloading/uploading a file, removing all the already received packets and ending the connection.

- MALFORMED PACKET (ERR TYPE: 0x05)

The error occurs when a received packet is malformed (either cannot be parsed or presents an incorrect checksum). MUST result in sending an error packet with the sequence number (SEQ) in the subheader payload from the receiving side. The error packet MAY also contain some additional information about the malformation in the payload of its subheader. Receiving a malformed packet MUST NOT result in sending an ACK packet by the receiving side to cause resending the packet by the sending side.