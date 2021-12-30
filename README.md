# epagneul

Epagneul is a tool to visualize and investigate windows event logs.

![layout](https://github.com/jurelou/epagneul/blob/master/images/layout.png?raw=true)

## Deployment

Requires docker and docker-compose to be installed.

### Installing

```
make
```

This will install:
- epagneul web UI (port 8080)
- epagneul backend (port 8000)
- neo4j (port 7474)

When installing on a server, you need to modify `VUE_APP_BASE_URL=http://<server name>:8000/api` in your `docker-compose.yaml`.


## todos

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

## Known bugs

- [ ] When multiple files are uploaded, properties will be overwritten

## References:

- https://adsecurity.org/wp-content/uploads/2017/04/2017-BSidesCharm-DetectingtheElusive-ActiveDirectoryThreatHunting-Final.pdf
- https://github.com/JPCERTCC/LogonTracer

## Built With

* [Vue.js](https://v3.vuejs.org/) - The web framework used
* [Cytoscape.js](https://js.cytoscape.org/) - Library used for visualisation and analysis
* [neo4j](https://neo4j.com/) - Backend database
* [evtx](https://github.com/omerbenamram/evtx) - Parser for the windows XML EventLog format

## Authors

* **Louis** - *Initial work* - [jurelou](https://github.com/jurelou)
