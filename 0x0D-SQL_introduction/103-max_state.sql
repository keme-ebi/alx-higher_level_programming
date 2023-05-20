-- displays the max temperature of each state ordered by state name
SELECT state, MAX(value) AS 'max_temp'
	FROM temperatures
	ORDER BY state;
