-- script that lists all shows contained in the database
SELECT tvs.title, tvg.genre_id FROM tv_shows AS tvs
	LEFT OUTER JOIN tv_show_genres AS tvg
	ON tvs.id = tvg.show_id
	ORDER BY tvs.title, tvg.genre_id ASC;
