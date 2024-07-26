"""
A047 - https://www.acmicpc.net/problem/11721
"""
def problem_11721(word):
    return "\n".join([word[i:i+10] for i in range(0, len(word), 10)])
