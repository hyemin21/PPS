def solution(s):
    return s.isdigit() and len(s) in [4, 6]

s = "a234"
print(solution(s))  
