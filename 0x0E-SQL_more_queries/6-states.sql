-- a script that creates the database hbtn_0d_usa and the table states in the database
-- The id would be unique and be a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	`id` INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
