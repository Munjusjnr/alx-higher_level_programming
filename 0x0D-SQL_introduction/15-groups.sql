--  a script that lists number of records with same score in the second_table
-- using different commands to execute this
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
