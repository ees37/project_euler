# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# initialize 
import time
start = time.time()
result = 0

# do work
def isPrime(num):
    maxPossibleFactor = int(num**0.5)
    i = 2
    while i <= maxPossibleFactor:
        if num % i == 0:
            return False
        i +=1
    return True

for i in range(2,2000000):
    if isPrime(i):
        result += i

# show result
print(result)
totalMs = (time.time() - start)
print("solved in " + str(totalMs) + " s")
