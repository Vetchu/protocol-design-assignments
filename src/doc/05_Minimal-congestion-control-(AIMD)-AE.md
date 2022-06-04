Sender-side MUST provide a congestion control mechanism for every connection and the mechanism MUST include the following algorithms:
- Slow Start
- AIMD
- Fast Retransmit
- Fast Recovery
The algorithms characterize TCP Reno [FF96]  which is supported as the minimal congestion control by the protocol. The client MAY choose a different congestion controller as long as those algorithms are still included in the controller of choice. 