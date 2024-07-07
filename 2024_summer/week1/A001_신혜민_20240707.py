'''
A001 - Assign Cookies 
최대한 많은 아이들에게 만족할 만한 쿠키를 주어야 한다. 
쿠키 사이즈 (int[ ] g)와 아이들이 만족하는 쿠키 사이즈(int[ ] s)가 매개변수로 주어지는 함수를 작성한다.
'''

def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i

# 예제
g = [1, 2, 3]
s = [1, 1]
print(findContentChildren(g, s))  
