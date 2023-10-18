-- script that lists all cities of California that can be found in the database.
SELECT id, name FROM cities WHERE id=(
	SELECT id FROM states WHERE name="California") ORDER BY cities.id;
