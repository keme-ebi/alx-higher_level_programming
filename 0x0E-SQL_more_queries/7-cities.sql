-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table 'cities' in the hbtn_0d_usa database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
	(id INT AUTO_INCREMENT PRIMARY KEY,
		FOREIGN KEY(state_id) NOT NULL REFERENCES states(id),
		name VARCHAR(256) NOT NULL);
