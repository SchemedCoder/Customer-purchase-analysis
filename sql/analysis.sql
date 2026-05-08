-- Total purchase by category
SELECT category, SUM(amount)
FROM purchases
GROUP BY category;

-- High-value customers
SELECT *
FROM purchases
WHERE amount > 1000;

-- Avg purchase amount
SELECT AVG(amount)
FROM purchases;
