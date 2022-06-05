## Reliability

As UDP itself provides no reliability, the protocol is equipped with properties which should provide basic reliability measures, such: 

### Acknowledgements

After receiving a packet, the receiving side MUST send an ACK packet in response. If no ACK packet is received 5 seconds after sending a packet, the sender MUST retransmit the packet.

### Timeouts

The protocol is equipped with the mechanism of timeouts. A timeout should occur:
- 5 seconds after sending an INIT packet in downloading mode if no DATA packet has been received
- 30 seconds after the last received packet if it was not a packet ending the connection