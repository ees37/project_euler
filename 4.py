# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# initialize 
import time
start = time.time()
result = 0

# do work
def is_palindrome(num):
    numStr = str(num)
    if numStr == numStr[::-1]:
        return True
    return False

palindromes = []
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if is_palindrome(product):
            palindromes.append(product)

result = max(palindromes)

# show result
print(result)
totalS = (time.time() - start)
print("solved in " + str(totalS) + " s")

