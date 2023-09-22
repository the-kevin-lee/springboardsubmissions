-- write your queries here

--1
SELECT *
FROM owners o
LEFT JOIN vehicles v
ON o.id = v.owner_id;

--2
SELECT o.first_name, o.last_name, COUNT(*) AS count
FROM owners o
JOIN vehicles v
ON o.id = v.owner_id
GROUP BY o.first_name, o.last_name
ORDER BY o.first_name ASC;


--3
SELECT o.first_name, o.last_name, AVG(v.price) AS average_price, COUNT(*) AS count
FROM owners o
JOIN vehicles v
ON o.id = v.owner_id
GROUP BY o.first_name, o.last_name
HAVING COUNT(*) > 1 AND AVG(v.price) > 10000
ORDER BY o.first_name DESC;
