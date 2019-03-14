#! /bin/bash

docker-compose up -d

docker exec -it docker_mongo mongo
