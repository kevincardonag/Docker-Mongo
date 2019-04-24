#!/bin/bash

sudo apt-get install default-jre
cd apache-jena-fuseki-3.10.0
./fuseki-server --file=json-to-ttl.ttl /estudio-cancer


