#!/bin/env bash
psql -U postgres -c "CREATE USER $DB_USER PASSWORD '$DB_PASS'"
psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"

# The Postgres image loads by default all the scripts in the 
# /docker-entrypoint-initdb.d directory, let’s create a simple 
# script that will create a user and a database using the 
# information from the env file

# requiere chmod a+rx postgres/docker-entrypoint-initdb.d/myproject_web.sh