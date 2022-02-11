-- Task 8
-- MySQL script to list all cities in California
SELECT id, name FROM cities
WHERE state_id IN
(SELECT id FROM states WHERE name = "California")
ORDER BY id ASC, name;
