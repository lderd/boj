-- 코드를 입력하세요
SELECT product_id, product_name, sum(total_sales) as total_sales FROM (
SELECT a.product_id, a.product_name, (a.price * b.amount) as total_sales
FROM food_product a, food_order b
WHERE to_char(b.PRODUCE_DATE, 'yyyy-mm') like '2022-05' and a.product_id = b.product_id
)
GROUP BY product_id, product_name
ORDER BY total_sales DESC, product_id;