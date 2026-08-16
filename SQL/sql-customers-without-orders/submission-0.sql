-- Write your query below
SELECT ct.name 
FROM customers AS ct LEFT JOIN orders AS ot
ON ct.id = ot.customer_id
WHERE ot.customer_id IS NULL;
