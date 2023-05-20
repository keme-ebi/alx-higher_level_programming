-- displays the top 3 cities temperature during July and August ordered by temperature descending
SELECT city, AVG(value) AS 'avg_temp'
	FROM temperatures
	WHERE month = 'July' OR month = 'August'
	GROUP BY city LIMIT 3
	ORDER BY avg_temp DESC;
