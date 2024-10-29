"""
https://school.programmers.co.kr/learn/courses/30/lessons/301647
프로그래머스 - 부모의 형질을 모두 가지는 대장균 찾기
"""
  
SELECT 
    c.ID, c.GENOTYPE, p.GENOTYPE AS PARENT_GENOTYPE
FROM 
    ECOLI_DATA c
JOIN 
    ECOLI_DATA p 
ON 
    c.PARENT_ID = p.ID
WHERE 
    (c.GENOTYPE & p.GENOTYPE) = p.GENOTYPE
ORDER BY 
    c.ID;
