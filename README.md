<p align="center"><img width="100" src="https://github.com/jurelou/epagneul/blob/dev-0.2.0/images/logo-rounded.png?raw=true" alt="Vue logo"></p>
<h2 align="center">epagneul</h2>

<div align="center">
 <p>
  <strong>
    Epagneul is a tool to visualize and investigate windows event logs.
  </strong>
 </p>
 <p>
  <img width="100" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336">
  <img width="100" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  <img width="100" src="http://www.mypy-lang.org/static/mypy_badge.svg">
  <img width="100" src="https://img.shields.io/badge/security-bandit-yellow.svg">
  <img width="100" src="https://img.shields.io/badge/python-3.8-blue">
 </p>
</div>


![layout](https://github.com/jurelou/epagneul/blob/master/images/layout.png?raw=true)


## Deployment

Requires docker and docker-compose to be installed.

### Installing

```
make
```

## Offline deployment

On a machine connected to internet, build an offline release:

```
make release
```
This will create a `release` folder containing ready to go docker images.
Copy the project to your air gapped machine then run:

```
make load
make
```

This will install:
- epagneul web UI (port 8080)
- epagneul backend (port 8000)
- neo4j (port 7474)

When installing on a server, you need to modify `VUE_APP_BASE_URL=http://<server name>:8000/api` in your `docker-compose.yaml`.


## todos

- [x] Better SID corelations
- [x] add edge tips
- [x] Label propagation algorithm
- [x] PageRank
- [x] Add missing events IDs (sysmon)
- [ ] hidden markov chains
- [ ] Display a timeline of logons / at least a summary graph
- [ ] check out: https://github.com/ahmedkhlief/APT-Hunter
- [ ] Import data from ELK / splunk
- [ ] detect communities using louvain
- [ ] Proper conversion of known SIDS / security principals, ...
- [ ] Document evtx filtering using `3,4648,4624,4625,4672,4768,4769,4771,4776`

## Known bugs

- The `count` value on edges does not update based on the selected timeline

## References:

- https://adsecurity.org/wp-content/uploads/2017/04/2017-BSidesCharm-DetectingtheElusive-ActiveDirectoryThreatHunting-Final.pdf
- https://github.com/JPCERTCC/LogonTracer

## Built With

* [Vue.js](https://v3.vuejs.org/) - The web framework used
* [Cytoscape.js](https://js.cytoscape.org/) - Library used for graph visualisation and analysis
* [d3](https://d3js.org/) - Used to display the timeline
* [neo4j](https://neo4j.com/) - Backend database
* [evtx](https://github.com/omerbenamram/evtx) - Parser for the windows XML EventLog format

## Authors

* **jurelou** - *Initial work* - [jurelou](https://github.com/jurelou)

