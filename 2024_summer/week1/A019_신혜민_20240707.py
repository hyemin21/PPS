def count_digits(a, b, c):
    result = str(a * b * c)
    count = [0] * 10
    for digit in result:
        count[int(digit)] += 1
    return count

a, b, c = 150, 266, 427
print(count_digits(a, b, c))  
