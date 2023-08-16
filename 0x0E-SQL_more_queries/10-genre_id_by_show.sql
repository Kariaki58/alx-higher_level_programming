-- Genre ID by show
SELECT tvs.title, tvg.genre_id FROM tv_shows AS tvs
	INNER JOIN tv_show_genres AS tvg
	ON tvs.id = tvg.show_id
	ORDER BY tvs.title, tvg.genre_id;
