def find_top_chef(scores: list) -> tuple:
    total_scores = [sum(score) for score in scores]
    winner = total_scores.index(max(total_scores)) + 1
    return winner, max(total_scores)