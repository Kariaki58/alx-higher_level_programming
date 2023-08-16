-- Number of shows by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS counter
       FROM tv_show_genres
       INNER JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       GROUP BY tv_genres.name
       ORDER BY counter DESC;
