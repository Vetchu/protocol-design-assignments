## Connections

Each packet sent MUST belong to some connection, i.e. have the ConnectionID field. They identify the particular connection this packet belongs to.

The connection MUST begin with INIT handshake specifying the ConnectionID used further. Each packet in this connection MUST contain the same ConnectionID identifier. There can never be two same ConnectionID identifiers for two different connections for every client and every server. Regardless of any other fields, the ConnectionID specifies a single client-server connection and MUST be treated as such for both sides of it.

### Connection Process

Each connection MUST begin with INIT packet specifying the version, ConnectionID and FileID proposed by the client. The error handling for these are described in another section. If the handshake completes successfully, the first data packet MUST be sent within 5 second window to the other side, or the connection is considered lost. If within 30 seconds no ACK or further data is transmitted from the other side, the connection is considered lost. If either side sents the CONN_ABORT error, both MUST consider the connection to be lost.

The connection is considered complete once the DATA packet containing only headers arrive at the client side, and both sides MUST remove the connection in the same manner as if it was lost.

## Handling connection drop

The Server and Client agree on common unique number identifier for a connection. If a connection fails, the Server and Client retain the identifier stored with expiration time of 30 seconds. If after this time the connection is not reestablished, the connection is lost and should be removed from both client and server.

Reestablishing the connection happens by sending a special packet resuming the connection with identifier of connection and last acknowledged packet's sequence number. The Server has to reply with acknowledgment with its own last good packet number, and the lower number of these is taken as a starting point for further transfer.