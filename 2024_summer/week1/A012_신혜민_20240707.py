def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i:n:i] = [False] * len(range(i*i, n, i))
    return sum(primes)

n = 10
print(countPrimes(n))  
