n = 600851475143

while n%2 == 0:
  n /= 2
  highest = 2

for i in range(3, int(n**(1/2))+1, 2):
  if n == 1:
    break
  while n%i == 0:
    n /= i
    highest = i

print(highest)