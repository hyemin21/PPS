"""
A053 - https://www.acmicpc.net/problem/10828
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
