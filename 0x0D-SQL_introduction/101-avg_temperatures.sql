-- displays the average temperature (Fahrenheit) by city ordered by temperature descending
SELECT city, AVG(value) AS 'avg_tmp'
	from temperatures
	GROUP BY city
	ORDER BY avg_tmp DESC;
