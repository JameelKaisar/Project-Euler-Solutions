n = 2000000
primes = [1] * n
primes[0] = 0
s = 0

for i, j in enumerate(primes):
    if j == 0:
        continue
    for k in range(2*(i+1), n+1, i+1):
        if primes[k-1] != 0:
            primes[k-1] = 0
    s += i+1

print(s)