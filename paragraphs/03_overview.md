## Overview

XTP is not a general purpose protocol, in that it is aimed for file transfer. This document defines version 1 of XTP and in the future it may be possible that newer versions will extend the functionalities or deeply change the ones described in this document. To see the version independent properties, refer to [INVARIANTS].

XTP is a connection-oriented protocol that creates a stateful interaction between a client and server. For each file transfer there is a different connection and the terms "client" and "server" are relative to a single connection, so a client in a connection can be a server in another connection and vice versa.

[[Other info, maybe about the version, the structure of the packets, etc.]]

XTP packets are carried in UDP datagrams [UDP]. This has the advantage of being already widely supported but a vast majority of devices, without having a big overhead due to the simplicity of UDP. There is also no protocol between UDP and XTP and no protocol on top of it. Altought it might be possible to develop a protoocol on top of XTP, this should not be necessary in the majority of cases, since the protocol already satisfies the requirements for a file transfer and an additional protocol would add unnecessary overhead.

### Terms and definitions

The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**, **"SHOULD NOT"**, **"RECOMMENDED"**, **"NOT RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.