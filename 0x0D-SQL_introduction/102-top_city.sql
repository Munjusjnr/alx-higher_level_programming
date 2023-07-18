-- a script that displays the top 3 of cities temperature during July and August
-- displays  top temperatures in 3 cities
SELECT city, AVG(value) AS `average_temp` FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY averge_temp DESC LIMIT 3;
