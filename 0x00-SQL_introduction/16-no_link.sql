-- Task 16
-- MySQL script to list all records of second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
