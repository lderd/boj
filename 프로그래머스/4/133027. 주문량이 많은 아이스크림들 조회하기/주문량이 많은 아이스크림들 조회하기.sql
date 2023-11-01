-- 코드를 입력하세요
SELECT flavor from(
SELECT flavor
FROM (SELECT flavor, total_order from first_half
    union all
    SELECT flavor, total_order from july b)
group by flavor
order by sum(total_order) DESC)
where ROWNUM <= 3
;