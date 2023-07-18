-- a script that displays the average temperature (Fahrenheit) by city ordered by temp
-- uses various commands to display the avg temps
SELECT city, AVG(value) AS `avg_temp` FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
