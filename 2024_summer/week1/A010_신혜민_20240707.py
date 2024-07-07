def solution(s):
    length = len(s)
    min_len = length
    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1
        for j in range(step, length, step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count > 1 else prev
        min_len = min(min_len, len(compressed))
    return min_len

s = "aabbaccc"
print(solution(s))  