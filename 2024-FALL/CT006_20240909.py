"""
https://school.programmers.co.kr/learn/courses/30/lessons/176963
프로그래머스 - 추억점수 
"""

def solution(name, yearning, photo):
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    result = []
    for p in photo:
        score = sum(yearning_dict.get(person, 0) for person in p)
        result.append(score)
    
    return result