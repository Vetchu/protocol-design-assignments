# Transfer in both directions

The protocol allows transferring files in both directions (downloading and uploading).

Uploading files requires adding a subheader to the INIT packet with TYPE set as 0x01 and an empty payload to inform the server that the client will be uploading the file. During uploading the FILE ID field presents the path where the file will be located. The server checks if such file already exists and if so, sends back an error packet FILE EXISTS. If no such file exists, the server sends an ACK packet as a response and waits for the incoming DATA packets from the client. Each correctly received DATA packet should be acknowledged using the ACK packet. The transaction is finished from the client's side when a DATA packet containing only a header is sent.