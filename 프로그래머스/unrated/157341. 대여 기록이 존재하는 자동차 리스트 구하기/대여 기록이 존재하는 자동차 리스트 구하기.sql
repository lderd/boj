-- 코드를 입력하세요
SELECT DISTINCT RC.CAR_ID AS CAR_ID 
FROM CAR_RENTAL_COMPANY_CAR RC, CAR_RENTAL_COMPANY_RENTAL_HISTORY RH
WHERE RC.CAR_ID = RH.CAR_ID
AND EXTRACT (MONTH FROM RH.START_DATE) = 10
AND RC.CAR_TYPE LIKE '세단'
ORDER BY CAR_ID DESC;