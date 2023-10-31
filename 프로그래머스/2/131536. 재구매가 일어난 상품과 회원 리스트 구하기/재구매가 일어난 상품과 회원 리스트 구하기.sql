-- 코드를 입력하세요
select distinct USER_ID, PRODUCT_ID from 
    (SELECT USER_ID, PRODUCT_ID, count(PRODUCT_ID) as cnt
    FROM ONLINE_SALE
    group by user_id, product_id)
where cnt >= 2
order by USER_ID, PRODUCT_ID desc;