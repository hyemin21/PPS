def room_number(n):
    count = [0] * 10
    for digit in str(n):
        count[int(digit)] += 1
    six_nine = (count[6] + count[9] + 1) // 2
    count[6] = count[9] = six_nine
    return max(count)

n = 6699
print(room_number(n))  
