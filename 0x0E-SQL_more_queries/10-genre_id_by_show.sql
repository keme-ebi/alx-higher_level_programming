-- lists all shows contained in hbtn_0d_tvshowa that have at least 1 genre linked
-- display: tv_shows.title - tv_show_genres.genre_id
-- results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.tile ASC, tv_show_genres.genre_id ASC;
