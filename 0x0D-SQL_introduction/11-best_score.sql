-- a script that lists all records with score >= 10 in the table second_table
-- listing all scores >= 10 in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;