"""
A050 - https://www.acmicpc.net/problem/5598
"""
# 문제 5598
def problem_5598(ciphertext):
    result = []
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - 68) % 26 + 65))
        else:
            result.append(char)
    return "".join(result)
