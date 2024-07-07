def above_average(scores):
    for score in scores:
        avg = sum(score[1:]) / score[0]
        above_avg = len([x for x in score[1:] if x > avg])
        print(f"{above_avg / score[0] * 100:.3f}%")

scores = [
    [5, 50, 50, 70, 80, 100],
    [7, 100, 95, 90, 80, 70, 60, 50]
]
above_average(scores)