-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table 'states' in the hbtn_0d_usa database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
	(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
