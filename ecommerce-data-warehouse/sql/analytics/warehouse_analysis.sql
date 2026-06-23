-- Total Revenue
SELECT SUM(amount) AS total_revenue
FROM fact_sales;

-- Revenue by Product
SELECT
    dp.product_name,
    SUM(fs.amount) AS revenue
FROM fact_sales fs
JOIN dim_product dp
    ON fs.product_id = dp.product_id
GROUP BY dp.product_name
ORDER BY revenue DESC;

-- Revenue by Payment Method
SELECT
    pm.payment_method,
    SUM(fs.amount) AS revenue
FROM fact_sales fs
JOIN dim_payment pm
    ON fs.payment_id = pm.payment_id
GROUP BY pm.payment_method
ORDER BY revenue DESC;

-- Top Customers
SELECT
    dc.customer_name,
    SUM(fs.amount) AS total_spent
FROM fact_sales fs
JOIN dim_customer dc
    ON fs.customer_id = dc.customer_id
GROUP BY dc.customer_name
ORDER BY total_spent DESC;