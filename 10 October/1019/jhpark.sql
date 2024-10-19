# -- 코드를 작성해주세요
SELECT DISTINCT A.ID, A.EMAIL, A.FIRST_NAME, A.LAST_NAME
FROM DEVELOPERS A
JOIN SKILLCODES B
ON A.SKILL_CODE = A.SKILL_CODE | B.CODE
WHERE B.CATEGORY LIKE 'Front End'
ORDER BY A.ID