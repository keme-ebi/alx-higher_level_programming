-- lists all records of the table second_table
-- don't list rows without a name value
-- result displays the score and the name
-- records are listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
