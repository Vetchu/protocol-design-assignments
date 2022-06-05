## General mechanism

In this section, the general mechanism of the model is described of {{NAME}} is described. The interactions between the client and server are therfore here described.

### Connection establishment

The client sends an *INIT packet* to the server. The packet will contain the following information:
- version
- proposed connection ID
- operation to be performed (e.g. download, file list)

The server will read the version. If the version is not supported, the server will send an *ERROR packet* of type *INCORRECT VERSION*, specifying which versions the server supports. If the version is supported, then the server will parse the rest of the packet based on the version itself. For the version 1, specified in this document, the server will create a connection with the proposed connection ID. If this is not possible (i.e. the connection already exists), the server will send an *ERROR packet* of type *INCORRECT CONNECTION*, possibly specifying also a valid connection id. The server will ultimately look at the operation, performing it in base of the type of operation. In case it is a file download of a listing of files, the server will start sending the data.

When the operation is performed, or case of an error or an abort, the connection will be closed, coming back to the initial state.