

DROP TABLE IF EXISTS regions, users, categories, posts;
DROP DATABASE craigslist_db;
CREATE DATABASE craigslist_db;
\c craigslist_db




CREATE TABLE regions(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    preferred_region_id INT REFERENCES regions(id) ON DELETE SET NULL
);


CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE POSTS (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(100) NOT NULL,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    region_id INT REFERENCES regions(id) ON DELETE SET NULL,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL
);



INSERT INTO regions(name)
VALUES
('San Francisco'),
('New York'),
('Atlanta'),
('Boston'),
('Los Angeles');


INSERT INTO users(username, preferred_region_id)
VALUES
('Joe Schmoe', 1),
('Arnold Schwarzenegger', 5),
('Joe Pesci', 2),
('Rick Roll', 3),
('Matt Damon', 4);

INSERT INTO categories(name)
VALUES
('Rentals'),
('Goods'),
('Personal'),
('Jobs');


INSERT INTO POSTS (title, description, location, user_id, region_id, category_id)
VALUES 
    ('Spacious 2-bedroom apartment for rent', 'Renting out a spacious 2-bedroom apartment in a great location. Perfect for families or roommates.', 'San Francisco, CA', 1, 1, 1),
    ('Gently used couch for sale', 'Selling a gently used couch in great condition. Comes from a smoke-free and pet-free home.', 'New York, NY', 2, 2, 2),
    ('Personal trainer for hire', 'Offering personal training services for individuals or small groups. Get in shape and feel great!', 'Atlanta, GA', 3, 3, 3),
    ('Part-time receptionist needed', 'Looking for a part-time receptionist to join our team. Must have excellent communication skills and be able to multitask.', 'Boston, MA', 4, 4, 4),
    ('Brand new iPhone 12 Pro Max', 'Selling a brand new iPhone 12 Pro Max in its original packaging. Unlocked and ready to use with any carrier.', 'Los Angeles, CA', 5, 5, 2);