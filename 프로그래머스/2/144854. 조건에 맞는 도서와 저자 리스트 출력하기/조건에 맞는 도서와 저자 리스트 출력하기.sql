-- 코드를 입력하세요
SELECT a.book_id, b.author_name, to_char(a.published_date, 'yyyy-mm-dd') as published_date
from book a, author b
where a.category like '경제' and a.author_id = b.author_id
order by a.published_date;