"""
A046 - https://www.acmicpc.net/problem/1159
"""
def problem_1159(names):
    from collections import defaultdict
    count = defaultdict(int)
    for name in names:
        count[name[0]] += 1
    result = sorted([char for char in count if count[char] >= 5])
    if result:
        return "".join(result)
    else:
        return "PREDAJA"
