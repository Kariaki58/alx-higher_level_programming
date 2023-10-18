-- lists all records that has a name
SELECT score, name FROM second_table WHERE name != "" OR name = NULL ORDER BY score DESC;
