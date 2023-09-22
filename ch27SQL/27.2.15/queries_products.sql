-- Inserts a new product into the products table with the name 'chair', a price of 44.00, and cannot be returned.
INSERT INTO products (name, price, can_be_returned) 
VALUES ('chair', 44.00, false);

-- Inserts a new product into the products table with the name 'stool', a price of 25.99, and can be returned.
INSERT INTO products (name, price, can_be_returned)
VALUES ('stool', 25.99, true);

-- Inserts a new product into the products table with the name 'table', a price of 124.00, and cannot be returned.
INSERT INTO products (name, price, can_be_returned)
VALUES('table', 124.00, false);

-- Displays all columns and rows in the products table.
SELECT * FROM products;

-- Selects the name column from the products table.
SELECT name FROM products;

-- Selects the name and price columns from the products table.
SELECT name, price FROM products;

-- Inserts a new product into the products table with the name 'Super Cool Glasses', a price of 500.00, and cannot be returned.
INSERT INTO products (name, price, can_be_returned)
VALUES ('Super Cool Glasses', 500.00, false);

-- Selects the name column from the products table where can_be_returned is true.
SELECT name FROM products WHERE can_be_returned = true;

-- Selects the name column from the products table where price is less than 44.00.
SELECT name FROM products WHERE price < 44.00;

-- Selects the name and price columns from the products table where price is between 22.50 and 99.99.
SELECT name, price FROM products WHERE price BETWEEN 22.50 AND 99.99;

-- Updates the price column of all rows in the products table to 20.00.
UPDATE products SET price = 20.00;

-- Deletes all rows from the products table where price is less than 25.00.
DELETE FROM products WHERE price < 25.00;

-- Updates the price column of all rows in the products table to 20.00.
UPDATE products SET price = 20.00;

-- Updates the can_be_returned column of all rows in the products table to true.
UPDATE products SET can_be_returned = true;