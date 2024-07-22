def problem_writing(d: int, h: int, s1: int, s2: int) -> tuple:
    happy_prob = [s1, s2]
    sad_prob = [s2, s1]

    for _ in range(d):
        new_happy = happy_prob[0] * happy_prob[1] / 100 + sad_prob[0] * (100 - happy_prob[1]) / 100
        new_sad = 100 - new_happy
        happy_prob = [new_happy, new_sad]
        sad_prob = [new_sad, new_happy]

    if h == 0:
        return (int(sad_prob[0]), int(happy_prob[0]))
    else:
        return (int(happy_prob[0]), int(sad_prob[0]))
