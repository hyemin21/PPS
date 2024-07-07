def intelligent_train(records):
    current = max_people = 0
    for out_, in_ in records:
        current += in_ - out_
        max_people = max(max_people, current)
    return max_people

records = [(0, 32), (3, 13), (28, 25), (39, 0)]
print(intelligent_train(records)) 
