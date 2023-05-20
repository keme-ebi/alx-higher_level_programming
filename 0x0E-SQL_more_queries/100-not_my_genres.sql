-- lists all genres not linked to the show Dexter from hbtn_0d_tvshowa database
-- display: tv_genres.name
-- results sorted in ascending order by the genre name
SELECT name
	FROM tv_genres
	RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE title = 'Dexter'
	ORDER BY name ASC;
