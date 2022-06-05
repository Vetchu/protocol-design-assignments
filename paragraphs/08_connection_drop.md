## Connection drop handling

The Server and Client agree on common unique number identifier for a connection. If a connection fails, the Server and Client retain the identifier stored with expiration time of 30 seconds. If after this time the connection is not reestablished, the connection is lost and should be removed from both client and server.

Reestablishing the connection happens by sending a special package resuming the connection with identifier of connection and last acknowledged packet's sequence number. The Server has to reply with acknowledgment with its own last good packet number, and the lower number of these is taken as a starting point for further transfer.