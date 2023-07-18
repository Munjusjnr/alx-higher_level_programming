-- a script that lists all records of the table second_table of the database
-- list should be without those with null name values in descending order by scores
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
