## Connections

Each packet sent MUST belong to some connection, i.e. have the ConnectionID field. They identify the particular connection this packet belongs to. 

The connection MUST begin with INIT handshake specifying the ConnectionID used further. Each packet in this connection MUST contain the same ConnectionID identifier. There can never be two same ConnectionID identifiers for two different connections for every client and every server. Regardless of any other fields, the ConnectionID specifies a single client-server connection and MUST be treated as such for both sides of it. 

### Connection Storage

Each connection SHOULD be stored as (Version,ConnectionID,FileID) Tuple, and MAY be accessed by hashing the ConnectionID in the global hashmap containing all present connections. If the connection is considered lost, the program MUST remove any object referring to it, such as identifiers and file uploaded/downloaded. 

### Connection Process

Each connection MUST begin with INIT packet specifying the version, ConnectionID and FileID proposed by client. The error handling for these are described in another section. If the handshake completes successfully, the first data packet MUST be sent within 5 second window to the other side, or the connection is considered lost. If within 30 seconds no ACK or further data is transmitted from the other side, the connection is considered lost. If either side sents the CONN_ABORT error, both MUST consider the connection to be lost.

The connection is considered complete once the DATA packet containing only headers arrive at the client side, and both sides MUST remove the connection in same manner as if it was lost.
