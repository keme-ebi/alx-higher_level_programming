-- displays all records of the table second_table with a score >= 10
-- displays in the order (score and name)
-- records are ordered by the top score
SELECT score, name FROM second_table HAVING score >= 10 ORDER BY score DESC, name DESC;
