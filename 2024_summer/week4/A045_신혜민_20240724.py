'''
A045 - https://www.acmicpc.net/problem/1157
'''
def problem_1157(word):
    word = word.upper()
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    max_count = max(count.values())
    max_chars = [char for char in count if count[char] == max_count]
    if len(max_chars) > 1:
        return "?"
    else:
        return max_chars[0]
