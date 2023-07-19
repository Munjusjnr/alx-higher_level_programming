-- a script that lists all cities contained in the database hbtn_0d_usa
-- using the join command
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
