-- Temperature #1
USE hbtn_0c_0
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=8 OR month=7 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
