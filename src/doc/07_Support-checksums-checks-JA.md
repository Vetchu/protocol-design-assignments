# Checksums

This protocol features the verification of transmitted data. The Client shall receive the data along the SHA256 checksum of the file. The Client shall then verify that the file has the same checksum value as the one received from the Server. 

This shall be done after receiving final acknowledgement of file received from the Server. The Client may request another copy of checksum to assure that the transmition did not impact the checksum received. After verifying the checksum, Client sends confirmation of file successfully received to the server. The Server shall then remove file from the buffer of "to be sent" files.