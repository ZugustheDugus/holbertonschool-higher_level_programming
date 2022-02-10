-- Task 11
-- MySQL script to list all scores >= 10 in second table
SELECT
	score, name
FROM
	second_table
WHERE
	score >= 10
ORDER BY
      score DESC
