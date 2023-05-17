-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table 'states'
CREATE TABLE IF NOT EXISTS states
	(id INT PRIMARY KEY, name VARCHAR(256) NOT NULL);
