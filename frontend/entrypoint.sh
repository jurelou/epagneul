#!/bin/sh

quasar build
quasar serve ./dist/spa --port 8080 --hostname 0.0.0.0 --history