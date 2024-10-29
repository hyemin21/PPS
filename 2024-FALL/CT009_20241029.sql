"""
https://school.programmers.co.kr/learn/courses/30/lessons/298515
잡은 물고기 중 가장 큰 물고기의 길이 구하기
"""

SELECT 
    ROUND(AVG(COALESCE(LENGTH, 10)), 2) AS AVERAGE_LENGTH
FROM 
    FISH_INFO;
