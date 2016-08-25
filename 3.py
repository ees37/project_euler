# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# initialize
import time
start = time.time()
result = 0

# do work
def isPrime(num):
    maxPossibleFactor = int(num**0.5)
    i = 2
    while i < maxPossibleFactor:
        if num % i == 0:
            return False
        i +=1
    return True

def getPrimeFactors(num):
    primeFactors = []
    maxPossibleFactor = int(num**0.5)
    i = 2
    while i < maxPossibleFactor:
        if num % i == 0:
            factor1 = i
            factor2 = num / i  
            if isPrime(factor1):
                primeFactors.append(factor1)
            if isPrime(factor2):
                primeFactors.append(factor2)
        i += 1
    return primeFactors

primeFactors = getPrimeFactors(600851475143)
result = max(primeFactors)

# show result
print(result)
totalS = (time.time() - start)
print("solved in " + str(totalS) + " s")
