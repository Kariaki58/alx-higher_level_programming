-- script that lists all cities contained in database;
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON cities.state_id=states.id
