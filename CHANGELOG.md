# Changelog
All notable changes to this project will be documented in this file.

## [x.x.x] - x

### Added
- x

### Changed
- x


## [0.3.2] - 2021-11-01

### Changed
- frontend: changed colors, now using high contrast colors from d3
- Include neo4j dependencies for offline deployment
- Fixed minor bugs
- The "remove" button now really removed the data !

## [0.3.1] - 2021-09-01

### Changed
- Fixed visual bugs
- Fixed a bug where admin users were not correctly displayed

## [0.3.0] - 2021-09-01

### Added
- Sysmon event ID 3
- Documentation for offline deployment
- frontend: autocomplete when searching
- Deduplicate edges based on their `event_type` and show the count

### Changed
- fixed a bug where options for searching were not updated on refresh
- frontend: display edges using a list of toggles

## [0.2.0] - 2021-08-01

### Added
- frontend: edge tippy

### Changed
- refactor pydantic models

## [0.1.1] - 2021-08-01

### Added
- Rounded logo in the `README.md`

### Changed
- Fixed assignation to constant variables in `Home.vue`

## [0.1.0] - 2021-08-01

### Added
- frontend: Add the ability to search for specific machines
- frontend: Added timeline
- Added production build via `make prod`

### Changed
- Edges are now tagged with their timestamp. It allows to filter edges by timestamp.
- UI: Switched to a simpler left side panel in the visualisation page

## [0.0.1] - 2021-30-12
Initial release