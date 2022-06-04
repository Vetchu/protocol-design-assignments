People:
* __JACE__ = https://github.com/Vetchu
* __ALEK__ = https://github.com/AleksandraSwierkowska
* __EUGE__ = https://github.com/euberdeveloper

Groups:
* __JA__ = (JACE, ALEK) (EUGE)
* __AE__ = (JACE) (ALEK, EUGE)
* __JE__ = (JACE, EUGE) (ALEK)

The things to implement for each group are (things in italic should be banal):
* _UPD based_: **JE**
* _No protocols on top of UPD_: **JA**
* _No protocol on top of itself_: **AE**
* Recover from connection drops: **JA** **accepted**
* Support connection migration: **JE**
* Reliability (check also what do we want as reliability): **AE**
* Flow control: **JE** **started**
* Minimal congestion control (AIMD): **AE** **started**
* _No authentication, ecc. ecc._: **AE**
* Support checksums checks: **JA** **started**
* Support multiple (parallel/seq) transfers: **JE**
* Transfer in both directions: **JA** **started**
* Which error conditions and how to handle them: **AE** **started**
