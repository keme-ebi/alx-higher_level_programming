-- lists all Comedy shows, and all genres linked to that show from hbtn_0d_tvshowa database
-- display: tv_shows.title - tv_genres.name
-- results sorted in ascending order by the show title and genre name
SELECT title, name
	FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	ORDER BY title ASC, name ASC;
