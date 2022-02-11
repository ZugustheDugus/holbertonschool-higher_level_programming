-- Task 16
-- MySQL script to listall shows linked to their genres
SELECT shows.title, genre.name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS tvshowgenre
ON shows.id = tvshowgenre.show_id
LEFT JOIN tv_genres AS genre
ON tvshowgenre.genre_id = genre.id
ORDER BY shows.title ASC, genre.name ASC;
