#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE TABLE IF NOT EXISTS students (
		"id" VARCHAR PRIMARY KEY,
		"first_name" VARCHAR,
		"last_name" VARCHAR,
		"gender" VARCHAR,
		"address" VARCHAR,
		"date_of_birth" VARCHAR,
		"major" VARCHAR,
		"year_of_study" INTEGER,
		"gpa" DECIMAL,
		"enrollment_status" VARCHAR
	);
	CREATE USER docker WITH PASSWORD 'dockeriscool';
	GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO docker;
EOSQL