-- a script that creates the table unique_id on your MySQL server
-- A table of values with a unique default id
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
