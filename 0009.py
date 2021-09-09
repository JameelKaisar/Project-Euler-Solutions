class NoError(Exception):
    pass

try:
    for i in range(int(1000/3), 998):
        for j in range(2, min(i, 1000-i)):
            k = 1000 - (i+j)
            if i**2 + j**2 == k**2:
                print(i*j*k)
                raise NoError
except:
    pass