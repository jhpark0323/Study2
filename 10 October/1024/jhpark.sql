-- 코드를 입력하세요
SELECT NAME, COUNT(*)
FROM ANIMAL_INS
GROUP BY NAME
HAVING NAME IS NOT NULL AND
        COUNT(*) > 1
ORDER BY NAME