-- Temperatures 0
SELECT city, AVG(value) AS data FROM temperatures GROUP BY city ORDER BY data DESC;
