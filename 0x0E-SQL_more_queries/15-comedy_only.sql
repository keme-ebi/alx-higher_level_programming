-- lists all Comedy shows from hbtn_0d_tvshowa database
-- display: tv_shows.title
-- results sorted in ascending order by the show title
SELECT title
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE name = 'Comedy'
	ORDER BY title ASC;
