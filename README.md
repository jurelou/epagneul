# epagneul

Graph Visualization for windows event logs

![layout](https://raw.githubusercontent.com/jurelou/epagneul/main/images/layout.png)


# install

Requires docker and docker-compose to be installed.

```
make
```
This will install:
- epagneul web UI (port 8080)
- epagneul backend (port 8000)
- neo4j (port 7474)

When installing on a server, you need to modify `VUE_APP_BASE_URL=http://<server name>:8000/api` in your `docker-compose.yaml`.

## Supported events:

- 4624: Successful logon
- 4625: Logon failure
- 4768: Kerberos Authentication (TGT Request)
- 4769: Kerberos Service Ticket (ST Request)
- 4776: NTLM Authentication
- 4672: Assign special privileges
- 4648: Explicit credential logon
- 4771: Kerberos pre-authentication failed


# TODOs:

- [ ] Better SID corelations
- [ ] hidden markov chains
- [x] Label propagation algorithm / detect communities
- [ ] PageRank
- [ ] Add missing events IDs (sysmon)
- [ ] Display a timeline of logons
- [ ] check out: https://github.com/ahmedkhlief/APT-Hunter
- [ ] Import data from ELK / splunk
- [ ] detect communities using louvain
- [ ] make a nice logo https://github.com/reiinakano/arbitrary-image-stylization-tfjs
- [ ] add edge tippy
- [ ] Proper conversion of known SIDS / security principals, ...

# BUGS

- [ ] When multiple files are uploaded, properties will be overwritten

# References:

- https://adsecurity.org/wp-content/uploads/2017/04/2017-BSidesCharm-DetectingtheElusive-ActiveDirectoryThreatHunting-Final.pdf
- https://github.com/JPCERTCC/LogonTracer

# Why ?  
* https://jardinage.lemonde.fr/dossier-2599-chiens-chasse.html
* https://compare-breeds.com/fr/compare-fr/beagle/brittany/
