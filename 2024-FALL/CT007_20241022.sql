"""
2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수(count)를 출력하는 SQL
프로그래머스_특정 형질을 가지는 대장균 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/301646
"""

SELECT COUNT(*)
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0  
  AND ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0);  
