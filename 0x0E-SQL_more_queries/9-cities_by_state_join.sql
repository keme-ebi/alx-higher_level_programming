-- lists all cities contained in the database hbtn_0d_usa
SELECT id, name, states.name AS 'name' FROM cities
	INNER JOIN states USING (states.id)
	ORDER BY cities.id ASC;
