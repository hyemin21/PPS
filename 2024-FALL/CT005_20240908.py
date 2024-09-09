"""
https://school.programmers.co.kr/learn/courses/30/lessons/178870
프로그래머스 - 연속된 부분 수열의 합
"""

def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = [0, 0]

    while end < n:
        if current_sum == k:
            if end - start < min_length:
                min_length = end - start
                answer = [start, end]
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1

    return answer
