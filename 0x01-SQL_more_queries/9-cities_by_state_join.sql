-- Task 9
-- MySQL script to list all cities contained in a database by state
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC, cities.name, states.name;
