## Transmission of packets

The protocol's packets are carried in [UDP](https://www.rfc-editor.org/info/rfc768) datagrams to better facilitate deployment in existing systems and networks. The protocol is also supposed to reside in the top of the network stack, so that there is no need for an additional layer on top of it to download the files.