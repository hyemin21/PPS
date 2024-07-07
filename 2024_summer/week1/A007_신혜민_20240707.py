'''
A007 - 음계 판별하기
8개의 숫자를 입력 받고 이 숫자들이 오름차순 정렬일 경우 ascending, 내림차순 정렬 일 경우 descending, 이 둘이 아니라면 mixed를 출력한다.
'''

def check_scale(lst):
    if lst == sorted(lst):
        return "ascending"
    elif lst == sorted(lst, reverse=True):
        return "descending"
    else:
        return "mixed"

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(check_scale(lst)) 
