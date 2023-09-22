-- Comments in SQL Start with dash-dash --

-- 1. Finding app with ID of 1880
SELECT app_name FROM analytics WHERE id = 1880;

-- 2. Finding apps that were last updated on August 1, 2018
SELECT id, app_name FROM analytics WHERE last_updated = '2018-08-01';

-- 3. Count number of apps in each category with category and count displayed
SELECT category, COUNT(app_name)
FROM analytics
GROUP BY category
ORDER BY category DESC;

-- 4. Find top 5 most reviewed apps and the number of reviews for each
SELECT app_name, reviews
FROM analytics
ORDER BY reviews DESC
LIMIT 5;

-- 5. Find app with most reviews with a rating greater than 4.8

SELECT app_name, reviews
FROM analytics
WHERE rating > 4.8
ORDER BY reviews DESC
LIMIT 1;


-- 6. Find average rating for each category ordered by the highest to lowest rated.
SELECT category, AVG(rating) AS avg_rating
FROM analytics
GROUP BY category
ORDER BY avg_rating DESC;

-- 7. Fiund name, price, and rating for the most expensive app with a rating of less than 3
SELECT app_name, price, rating 
FROM analytics
WHERE rating < 3
ORDER BY price DESC
LIMIT 1;

-- 8. Find all the apps with a min_installs of less than 5 and have at least a rating -- > order by rating from most to least
SELECT app_name, min_installs, rating
FROM analytics
WHERE min_installs < 50
AND rating > 0
ORDER BY rating DESC;


-- 9. Find all the apps that have a rating less than 3 but at least 10_000 reviews
SELECT app_name, rating, reviews
FROM analytics
WHERE rating < 3
AND reviews >= 10000;

-- 10. Find the 10 most reviewed apps that are priced between 10 cents to a dollar
SELECT app_name, price, reviews
FROM analytics
WHERE price BETWEEN .10 AND 1.00
ORDER BY reviews DESC
LIMIT 10;

-- 11. Find the most out of date app
SELECT app_name, last_updated
FROM analytics
ORDER BY last_updated ASC
LIMIT 1;

-- 12. Find the most expensive app
SELECT app_name, price
FROM analytics
ORDER BY price DESC
LIMIT 1;

-- 13. Count all the reviews in the store
SELECT SUM(reviews)
FROM analytics;

-- 14. Find the number of apps within each category
SELECT category, COUNT(app_name) AS app_count
FROM analytics
GROUP BY category
HAVING COUNT(app_name) > 300;

-- 15. Selects the app with the highest proportion of minimum installs to reviews where the app has been installed at least 100_000 times
SELECT app_name, reviews, min_installs, (min_installs::FLOAT / reviews:: FLOAT) AS proportion
FROM analytics
WHERE min_installs >= 100000
ORDER BY proportion DESC
LIMIT 1;