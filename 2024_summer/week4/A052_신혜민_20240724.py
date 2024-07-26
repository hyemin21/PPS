"""
A052 - https://www.acmicpc.net/problem/8958
"""
# 문제 8958
def problem_8958(results):
    scores = []
    for result in results:
        score = 0
        current_streak = 0
        for char in result:
            if char == 'O':
                current_streak += 1
                score += current_streak
            else:
                current_streak = 0
        scores.append(score)
    return scores
"""
A052 - https://www.acmicpc.net/problem/10828
"""
# 문제 10828
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1