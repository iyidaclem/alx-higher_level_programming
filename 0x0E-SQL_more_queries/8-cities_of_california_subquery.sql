-- Select all the cities of california
SELECT id, cities.name
FROM states, cities
WHERE cities.state_id = states.id;
