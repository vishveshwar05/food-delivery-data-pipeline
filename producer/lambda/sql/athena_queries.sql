-- Count orders by stage
SELECT stage, COUNT(*) AS total_orders
FROM bronze_orders
GROUP BY stage;

-- Average delivery time
WITH order_times AS (
 SELECT order_id,
 MAX(CASE WHEN stage='ORDER_PLACED' THEN time END) AS placed,
 MAX(CASE WHEN stage='DELIVERED' THEN time END) AS delivered
 FROM silver_orders
 GROUP BY order_id
)
SELECT AVG(date_diff('minute', placed, delivered)) AS avg_delivery_time
FROM order_times;
