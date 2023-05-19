-- lists all shows contained in hbtn_0d_tvshowa that have at least 1 genre linked
-- display: tv_shows.title - tv_show_genres.genre_id
-- results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT title, genre_id
	FROM tv_show_genres
	LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id
	ORDER BY title ASC, genre_id ASC;
