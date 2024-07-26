"""
B024 - https://leetcode.com/problems/relative-ranks/description/
"""

def findRelativeRanks(score):
    sorted_scores = sorted(score, reverse=True)
    rank_map = {score: str(i+1) for i, score in enumerate(sorted_scores)}
    for i in range(len(sorted_scores)):
        if i == 0:
            rank_map[sorted_scores[i]] = "Gold Medal"
        elif i == 1:
            rank_map[sorted_scores[i]] = "Silver Medal"
        elif i == 2:
            rank_map[sorted_scores[i]] = "Bronze Medal"
    return [rank_map[s] for s in score]
