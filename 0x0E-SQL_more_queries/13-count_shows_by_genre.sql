-- lists all genres from hbtn_0d_tvshowa and displays the number of shows linked
-- display: first column as genre - second column as number_of_shows
-- if a show doesn't have a genre, it returns NULL
-- results sorted in desscending order by the number of shows linked
SELECT name AS 'genre', COUNT(show_id) AS 'number_of_shows'
	FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY 'number_of_shows' DESC;
