'''
A003 - Plus One
주어진 정수 배열을 하나의 정수 값이라고 생각했을 때, 그 정수에 1을 더한 값을 다시 배열의 형태로 return 하는 함수를 작성한다.
'''
def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]
