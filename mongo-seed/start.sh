#!/bin/bash

sleep 30
mongoimport --host mongodb --db articles --collection articles_collection --type json --file /file.json --jsonArray