-- Task 14
-- MySQL script to list all genres of "dexter"
SELECT a.name AS name FROM tv_genres AS a
JOIN tv_show_genres AS b
ON b.genre_id = a.id
JOIN tv_shows AS c
ON b.show_id = c.id 
WHERE c.title = 'Dexter'
ORDER BY a.name ASC;
