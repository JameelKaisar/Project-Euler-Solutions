chain = {}
start = -1
high = -1

for i in range(1, 1000000):
    n = i
    if i not in chain:
        chain[i] = 0
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n +1
        chain[i] += 1
        if n in chain:
            chain[i] += chain[n]
            break
    if chain[i] > high:
        high = chain[i]
        start = i

print(start)