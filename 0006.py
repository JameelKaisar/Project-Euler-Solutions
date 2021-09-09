num = 100

sum_of_squares = int((num*(num+1)*(2*num+1))/6)
square_of_sums = int(((num*(num+1))/2)**2)
difference = square_of_sums - sum_of_squares

print(difference)