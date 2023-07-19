-- a script that lists all genres from hbtn_0d_tvshows
-- list displays the number of shows linked to each
-- Results are ordered by descending number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
