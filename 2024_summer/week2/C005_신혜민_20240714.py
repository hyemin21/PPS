def solution(participant, completion):
    import collections
    p_count = collections.Counter(participant)
    c_count = collections.Counter(completion)
    for p in p_count:
        if p_count[p] != c_count[p]:
            return p
