-- Select all the cities of california
SELECT id, name
FROM cities
WHERE id = (
    SELECT id states where name  = 'California')
ORDER BY id asc;
