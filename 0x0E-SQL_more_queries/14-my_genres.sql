-- lists all genres of the show Dexter from hbtn_0d_tvshowa database
-- display: tv_genres.name
-- results sorted in desscending order by the genre name
SELECT name
	FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id
	WHERE title = 'Dexter'
	ORDER BY name ASC;