## Packets

The packets defined by the XTP protocol are defined in this section.

### Base header

All the packets share a common part in the header. In particular, they all begin with: 
- **type** _(X bytes)_: The type of the packet.
- **size** _(X bytes)_: The size of the header of the packet.
- **connection ID** _(X bytes)_: The connection ID of the packet.

Note: All the packets described below start with these fields.

### Data/ACK packet

- **seq** _(X bytes)_: The sequence number of the packet, telling which chunk is being processed.

### Special packet

A special packet is a packet that... TODO
    
### Init packet

It is used to establish a connection and perform a request to the server.

- **version** _(X bytes)_: The version of XTP that the client wants to use.
- **file id** _(X bytes)_: The file id that the client wants to download. If it is 0, the client requests the list of files in the server.

### Slow down packet

TODO

### Error packet

The error packet is used to report an error to the client. All the error packets start with the type of error, while the content might vary in base of that.

- **error type** _(X bytes)_: The type of the error.
  

## Checksums

The packets are incapsulated in UDP diagrams, that use a checksum to check for integrity of the transmitted data. For this reason and for the reliability of the protocol, XTP does not use any checksum.