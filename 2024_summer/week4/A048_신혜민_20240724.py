"""
A048 - https://www.acmicpc.net/problem/1316
"""
# 문제 1316
def problem_1316(words):
    def is_group_word(word):
        seen = set()
        prev_char = ""
        for char in word:
            if char != prev_char:
                if char in seen:
                    return False
                seen.add(char)
                prev_char = char
        return True

    return sum(1 for word in words if is_group_word(word))
