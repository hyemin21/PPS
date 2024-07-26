"""
A065 - https://www.acmicpc.net/problem/11650
"""
# 문제 11650
def problem_11650(points):
    return sorted(points, key=lambda point: (point[0], point[1]))
