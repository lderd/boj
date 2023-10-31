-- 코드를 입력하세요
select * from (
SELECT TO_CHAR(sales_date, 'YYYY-MM-DD') as sales_date, product_id, user_id, sales_amount
FROM online_sale
where TO_CHAR(sales_date, 'YYYY-MM-DD') like '2022-03%'
union all
SELECT TO_CHAR(sales_date, 'YYYY-MM-DD') as sales_date, product_id, NULL as user_id, sales_amount
FROM offline_sale
where TO_CHAR(sales_date, 'YYYY-MM-DD') like '2022-03%')
order by sales_date, product_id, user_id;