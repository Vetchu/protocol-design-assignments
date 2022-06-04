# Error conditions and handling them

The protocol handles five types of errors:
- INCORRECT CONNECTION ID

The error occurs when the CONNECTION ID field in an INIT PACKET sent by the client contains a number already used for another connection by the server. The server MUST send an error packet in which it MAY include a suggested CONNECTION ID in the payload of the subheader. The error causes the immediate end of the connection.


- INCORRECT VERSION

The error occurs when the VERSION field in an INIT PACKET sent by the client contains a version not accepted by the server. The server MUST send an error packet in which it MAY include a suggested VERSION in the payload of the subheader. The error causes the immediate end of the connection.


- FILE NOT FOUND

The error occurs when the FILE ID field in an INIT PACKET sent by the client contains a path to a non-existing file in the downloading mode or an existing file in the uploading mode. The server MUST send an error packet. The error causes the immediate end of the connection.

- ABORT DOWNLOAD

The error is caused by the ABORT DOWNLOAD error packet sent by either client or server. It causes immediate stopping of downloading/uploading a file, removing all the already received packets and ending the connection.

- MALFORMED PACKET

The error occurs when a received packet is malformed (either cannot be parsed or presents an incorrect checksum). MUST result in sending an error packet with the sequence number (SEQ) in the subheader payload from the receiving side. The error causes the immediate end of the connection.