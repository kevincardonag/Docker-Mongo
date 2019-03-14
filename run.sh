#! /bin/bash

docker-compose up -d

docker exec -it Docker-Mongo_mongodb_1 mongo
