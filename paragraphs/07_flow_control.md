# Flow Control

The Server sends packets with exponential rate. It means that it sends the messages in groups of 2^n, starting with n=0 and increasing it by 1 for every consequent group. After every packet group is sent, it doubles its sending rate until the client informs it about too many missing packets. The Server shall then halve its sending rate, while prioritizing resending packets missed (priority should be given to packets with a lower sequence number).

The Client MAY inform the server about percentage of missed packets once the average over last 1000 packets sent is greater than 10%. The special packet shall then be sent informing about the percentage of missed packets, so that the Server can adjust its sending speed.