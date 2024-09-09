"""
https://school.programmers.co.kr/learn/courses/30/lessons/181188
프로그래머스 - 요격시스템 
"""

def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_missile = -1
    
    for s, e in targets:
        if last_missile < s:
            answer += 1
            last_missile = e - 0.5  
    
    return answer
