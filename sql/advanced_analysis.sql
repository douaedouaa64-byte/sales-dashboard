SELECT 
    SUM(total) AS total_revenue,
    AVG(total) AS avg_order_value,
    COUNT(*) AS total_transactions
FROM sales;

SELECT 
    product_line,
    SUM(total) AS revenue,
    RANK() OVER (ORDER BY SUM(total) DESC) AS rank_product
FROM sales
GROUP BY product_line;

SELECT 
    strftime('%Y-%m', date) AS month,
    SUM(total) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

SELECT 
    customer_type,
    COUNT(*) AS nb_orders,
    AVG(total) AS avg_spending
FROM sales
GROUP BY customer_type;
