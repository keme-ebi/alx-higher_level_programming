-- lists all cities of California that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
	INNER JOIN states USING (states.id)
	ORDER BY cities.id ASC;
