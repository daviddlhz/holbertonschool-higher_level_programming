-- in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, count(score) AS number FROM second_table GROUP BY score DESC;
