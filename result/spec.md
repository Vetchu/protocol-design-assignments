# XTP - eXtendable Transfer Protocol

## Abstract

This document defines the XTP protocol. XTP is a protocol that allows a robust file transfer between two hosts. It provides reliability, support for multiple simultaneous transfers in both directions and a minimal congestion and flow control.

## Status of This Memo

This is an protocol created for the assignment of the course *"Protocol Design (IN2333)"* for the Summer Semester 2022 of TUM.

## Overview

XTP is not a general purpose protocol, in that it is aimed for file transfer. This document defines version 1 of XTP and in the future it may be possible that newer versions will extend the functionalities or deeply change the ones described in this document.

XTP is a connection-oriented protocol that creates a stateful interaction between a client and server. For each file transfer there is a different connection and the terms "client" and "server" are relative to a single connection, so a client in a connection can be a server in another connection and vice versa.

[[Other info, maybe about the version, the structure of the packets, etc.]]

XTP packets are carried in UDP datagrams [UDP]. This has the advantage of being already widely supported but a vast majority of devices, without having a big overhead due to the simplicity of UDP. There is also no protocol between UDP and XTP and no protocol on top of it. Altought it might be possible to develop a protoocol on top of XTP, this should not be necessary in the majority of cases, since the protocol already satisfies the requirements for a file transfer and an additional protocol would add unnecessary overhead.

### Terms and definitions

The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**, **"SHOULD NOT"**, **"RECOMMENDED"**, **"NOT RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

## General mechanism

In this section, the general mechanism of the model is described of XTP is described. The interactions between the client and server are therfore here described.

### Connection establishment

The client sends an *INIT packet* to the server. The packet will contain the following information:
- version
- proposed connection ID
- operation to be performed (e.g. download, file list)

The server will read the version. If the version is not supported, the server will send an *ERROR packet* of type *INCORRECT VERSION*, specifying which versions the server supports. If the version is supported, then the server will parse the rest of the packet based on the version itself. For the version 1, specified in this document, the server will create a connection with the proposed connection ID. If this is not possible (i.e. the connection already exists), the server will send an *ERROR packet* of type *INCORRECT CONNECTION*, possibly specifying also a valid connection id. The server will ultimately look at the operation, performing it in base of the type of operation. In case it is a file download of a listing of files, the server will start sending the data.

When the operation is performed, or case of an error or an abort, the connection will be closed, coming back to the initial state.

## Packets

The packets defined by the XTP protocol are defined in this section.

### Base header

All the packets share a common part in the header. In particular, they all begin with: 
- **type** _(1 byte)_: The type of the packet.
- **size** _(2 bytes)_: The size of the header of the packet.
- **connection ID** _(2 bytes)_: The connection ID of the packet.

Note: All the packets described below start with these fields.

### Data/ACK packet

- **seq** _(2 bytes)_: The sequence number of the packet, telling which chunk is being processed.

### Special packet

A special packet is a packet containing XHEAD field, which allows to add a subheader with additional information. 

- **XHEAD** 
  - TYPE _(2 bytes)_
  - SIZE _(2 bytes)_
  - PAYLOAD

    
### Init packet

It is used to establish a connection and perform a request to the server.

- **version** _(1 byte)_: The version of {{NAME}} that the client wants to use.
- **file id** _(unknown length, limited by '\n' character)_: The file id that the client wants to download. If it is 0, the client requests the list of files in the server.

### Slow down packet

It is used to support flow control and inform the sender about the ratio of missing packets.

- **miss ratio** _(2 bytes)_: Ratio of missed packets

### Error packet

The error packet is used to report an error to the client. All the error packets start with the type of error, while the content might vary in base of that.

- **error type** _(1 byte)_: The type of the error.
  
## Checksums

The packets are incapsulated in UDP diagrams, that use a checksum to check for integrity of the transmitted data. For this reason and for the reliability of the protocol, XTP does not use any checksum.
## Connections

Each packet sent MUST belong to some connection, i.e. have the ConnectionID field. They identify the particular connection this packet belongs to.

The connection MUST begin with INIT handshake specifying the ConnectionID used further. Each packet in this connection MUST contain the same ConnectionID identifier. There can never be two same ConnectionID identifiers for two different connections for every client and every server. Regardless of any other fields, the ConnectionID specifies a single client-server connection and MUST be treated as such for both sides of it.

### Connection Process

Each connection MUST begin with INIT packet specifying the version, ConnectionID and FileID proposed by the client. The error handling for these are described in another section. If the handshake completes successfully, the first data packet MUST be sent within 5 second window to the other side, or the connection is considered lost. If within 30 seconds no ACK or further data is transmitted from the other side, the connection is considered lost. If either side sents the CONN_ABORT error, both MUST consider the connection to be lost.

The connection is considered complete once the DATA packet containing only headers arrive at the client side, and both sides MUST remove the connection in the same manner as if it was lost.

## Handling connection drop

The Server and Client agree on common unique number identifier for a connection. If a connection fails, the Server and Client retain the identifier stored with expiration time of 30 seconds. If after this time the connection is not reestablished, the connection is lost and should be removed from both client and server.

Reestablishing the connection happens by sending a special packet resuming the connection with identifier of connection and last acknowledged packet's sequence number. The Server has to reply with acknowledgment with its own last good packet number, and the lower number of these is taken as a starting point for further transfer.

## Flow Control

The Server sends packets with exponential rate. It means that it sends the messages in groups of 2^n, starting with n=0 and increasing it by 1 for every consequent group. After every packet group is sent, it doubles its sending rate until the client informs it about too many missing packets. The Server shall then halve its sending rate, while prioritizing resending packets missed (priority should be given to packets with a lower sequence number).

The Client MAY inform the server about percentage of missed packets once the average over last 1000 packets sent is greater than 10%. The special packet shall then be sent informing about the percentage of missed packets, so that the Server can adjust its sending speed.

## Reliability

As UDP itself provides no reliability, the protocol is equipped with properties which should provide basic reliability measures, such: 

### Acknowledgements

After receiving a packet, the receiving side MUST send an ACK packet in response. If no ACK packet is received 5 seconds after sending a packet, the sender MUST retransmit the packet.

### Timeouts

The protocol is equipped with the mechanism of timeouts. A timeout should occur:
- 5 seconds after sending an INIT packet in downloading mode if no DATA packet has been received
- 30 seconds after the last received packet if it was not a packet ending the connection

## Error conditions and handling them

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

## References

[FF96] Fall, K. and S. Floyd, "Simulation-based Comparisons of Tahoe, Reno and SACK TCP", Computer Communication Review, July 1996, ftp://ftp.ee.lbl.gov/papers/sacks.ps.Z
[UDP] Postel, J., "User Datagram Protocol", STD 6, RFC 768, DOI 10.17487/RFC0768, August 1980, <https://www.rfc-editor.org/info/rfc768>.
[RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <https://www.rfc-editor.org/info/rfc2119>.
[RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <https://www.rfc-editor.org/info/rfc8174>.
