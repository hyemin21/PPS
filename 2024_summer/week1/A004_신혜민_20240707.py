'''
A004 - 나누어 떨어지는 숫자 배열
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환
'''
def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    return sorted(answer) if answer else [-1]

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor)) 
