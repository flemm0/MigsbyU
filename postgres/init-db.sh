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
	CREATE TABLE IF NOT EXISTS professors (
		"id" VARCHAR PRIMARY KEY,
		"title" VARCHAR,
		"first_name" VARCHAR,
		"last_name" VARCHAR,
		"gender" VARCHAR,
		"address" VARCHAR,
		"department" VARCHAR,
		"date_of_birth" DATE,
		"annual_salary" INTEGER
	);
	CREATE TABLE IF NOT EXISTS courses (
		"id" VARCHAR PRIMARY KEY,
		"name" VARCHAR,
		"units" INTEGER,
		"department" VARCHAR
	);
	CREATE TABLE IF NOT EXISTS takes (
		"student_id" VARCHAR,
		"course_id" VARCHAR,
		"semester" VARCHAR,
		PRIMARY KEY (student_id, course_id, semester),
		CONSTRAINT fk_student_id
			FOREIGN KEY (student_id) 
			REFERENCES students(id)
			ON DELETE SET NULL,
		CONSTRAINT fk_course_id
			FOREIGN KEY (course_id) 
			REFERENCES courses(id)
			ON DELETE SET NULL
	);
	CREATE TABLE IF NOT EXISTS teaches (
		"professor_id" VARCHAR,
		"course_id" VARCHAR,
		"semester" VARCHAR,
		PRIMARY KEY (professor_id, course_id, semester),
		CONSTRAINT fk_professor_id
		FOREIGN KEY (professor_id) 
		REFERENCES professors(id)
		ON DELETE SET NULL,
		CONSTRAINT fk_course_id
		FOREIGN KEY (course_id) 
		REFERENCES courses(id)
		ON DELETE SET NULL
	);
	CREATE USER docker WITH PASSWORD 'dockeriscool';
	GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO docker;
EOSQL