#!/bin/env bash
psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';"
psql -U postgres -c "ALTER ROLE $DB_USER SUPERUSER;"
psql -U postgres -c "CREATE EXTENSION postgis;"

psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
psql -U postgres -c "ALTER ROLE $DB_USER SET client_encoding TO 'utf8';"
psql -U postgres -c "ALTER ROLE $DB_USER SET timezone TO 'UTC';"




# The Postgres image loads by default all the scripts in the 
# /docker-entrypoint-initdb.d directory, let’s create a simple 
# script that will create a user and a database using the 
# information from the env file

# requiere chmod a+rx postgres/docker-entrypoint-initdb.d/myproject_web.sh