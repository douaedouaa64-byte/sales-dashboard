-- Top customers
SELECT 
    customer_type,
    SUM(total) AS total_spent
FROM sales
GROUP BY customer_type
ORDER BY total_spent DESC;

-- Revenue by city and product
SELECT 
    city,
    product_line,
    SUM(total) AS revenue
FROM sales
GROUP BY city, product_line
ORDER BY revenue DESC;

-- Subquery example
SELECT *
FROM sales
WHERE total > (
    SELECT AVG(total) FROM sales
);
