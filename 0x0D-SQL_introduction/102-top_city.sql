-- displays the top 3 cities temperature during July and August ordered by temperature descending
SELECT city, AVG(value) AS 'avg_temp'
	FROM temperatures
	WHERE year = 'July' OR 'August'
	GROUP BY city
	ORDER BY avg_temp DESC;
