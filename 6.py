# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# initialize 
import time
start = time.time()
result = 0

# do work
sequence = list(range(101))
def get_sum_of_squares():
    summ = 0
    for x in sequence:
        summ += (x**2)  
    return summ

def get_square_of_sum():
    summ = 0
    for x in sequence:
        summ += x
    return summ**2

result = get_square_of_sum() - get_sum_of_squares()

# show result
print(result)
totalMs = (time.time() - start)
print("solved in " + str(totalMs) + " s")
