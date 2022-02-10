-- Task 15
-- MySQL script to list the number of records of same score in second_table
SELECT score, COUNT(score)
AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
