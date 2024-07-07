def solution(N, stages):
    fail_rates = []
    total_users = len(stages)
    for i in range(1, N + 1):
        failed_users = stages.count(i)
        if total_users == 0:
            fail_rate = 0
        else:
            fail_rate = failed_users / total_users
        fail_rates.append((i, fail_rate))
        total_users -= failed_users
    fail_rates.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in fail_rates]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  
