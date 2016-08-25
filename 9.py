# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# initialize 
import time
start = time.time()
result = 0

# do work
def isPerfectSquare(x):
    sqrt = x**0.5
    if int(sqrt) == sqrt:
        return True
    return False

for a in range(0,1000):
    for b in range(a+1,a+1001):
        cSq = (a**2) + (b**2)
        c = cSq**0.5
        if isPerfectSquare(cSq) and a + b + c  == 1000:
            result = a * b * c
            break

# show result
print(result)
totalMs = (time.time() - start)
print("solved in " + str(totalMs) + " s")
