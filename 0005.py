primes = {2: 1}
for i in range(3, 21):
    for j in range(3, int(i**(1/2))+1, 2):
        temp = 0
        while i%j == 0:
            i /= j
            temp += 1
        if j not in primes or temp > primes[j]:
            primes[j] = temp
    temp = 0
    while i%2 == 0:
        i /= 2
        temp += 1
    if temp > primes[2]:
        primes[2] = temp
    if int(i) not in primes:
        primes[int(i)] = 1

answer = 1
for i, j in primes.items():
    answer *= i**j

print(answer)