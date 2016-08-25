

# initialize 
import time
start = time.time()
result = 0

# do work
def isPrime(num):
    maxPossibleFactor = int(num**0.5) + 1
    i = 2
    while i <= maxPossibleFactor:
        if num % i == 0:
            return False
        i +=1
    return True

num = 1
count = 0
while True:
    if isPrime(num):
        count += 1
        if count == 10001:
            result = num
            break
    num += 1

# show result
print(result)
totalMs = (time.time() - start)
print("solved in " + str(totalMs) + " s")
