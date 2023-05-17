-- lists the number of records with the same score in the table `second_table`
-- displays the scores in descending order
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score;
