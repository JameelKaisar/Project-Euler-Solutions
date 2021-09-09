from math import log


nth = 10001 # nth > 6
n = round(nth * log(nth * log(nth)))
primes = [1] * n
primes[0] = 0

for i, j in enumerate(primes):
    if j == 0:
        continue
    for k in range(2*(i+1), n, i+1):
        if primes[k-1] != 0:
            primes[k-1] = 0
    nth -= 1
    if not nth:
        print(i+1)
        break