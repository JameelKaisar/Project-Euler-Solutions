class NoError(Exception):
    pass

try:
    for i in range(999, 99, -1):
        for j in range(999, i-1, -1):
            if i*j == int(''.join(list(reversed(str(i*j))))):
                low = i
                high = j
                palindrome = i*j
                raise NoError
except NoError:
    pass

try:
    for i in range(924, int(palindrome/999), -1):
        for j in range(999, 962, -1):
            if i*j > 888888 and i*j == int(''.join(list(reversed(str(i*j))))):
                    palindrome = i*j
                    raise NoError
except NoError:
    pass

print(palindrome)