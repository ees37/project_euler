# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# initialize 
import time
start = time.time()
result = 0

# do work
range_to_check = [20, 18, 17, 16, 15, 14,13, 12, 11] # this excludes factors of numbers already in the range

def is_evenly_divisible_by_range(num):
    for i in range_to_check:
        if num % i != 0:
            return False
    return True

num = 1
while True:
   if is_evenly_divisible_by_range(num):
       result =  num * 19
       break
   num += 1

# show result
print(result)
totalMs = (time.time() - start)
print("solved in " + str(totalMs) + " s")

