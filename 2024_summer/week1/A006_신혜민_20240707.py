'''
A006 - 문자열 내 p와 y의 개수
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 
'''
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

s = "pPoooyY"
print(solution(s))  
