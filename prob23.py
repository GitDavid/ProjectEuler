#!/usr/bin/env python

import math

def isPrime(n):
    '''
    basic checks for lower numbers and all primes = 6k +/-1
    '''
    if n == 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n < 9:
        return True
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if (n % f == 0) or (n % (f + 2) == 0):
                return False
            f += 6
        return True

primesArr = []
for i in range(1, 28123):
    if isPrime(i):
        primesArr.append(i)

def d(n):
    '''sum of proper divisors less than n'''
    m = n
    i = 0
    sum = 1
    while n > 1:
        p = primesArr[i]
        pPower = p
        while n % p == 0:
            n /= p
            pPower *= p
        sum = sum * (pPower - 1) / (p -1)
        i += 1
    return sum - m

abundantArr = []

for i in range(1, 28123):
    if d(i) > i:
        abundantArr.append(i)

def sumArr(arr):
    total = 0
    for i in arr:
        total += i
    return total

grandTotal = sumArr(range(1, 28123))
abundantSums = set()
print grandTotal

for i in abundantArr:
    for j in abundantArr[abundantArr.index(i):]:
        if i + j >= 28123:
            break
        elif (i + j < 28123) and ((i + j) not in abundantSums):
            abundantSums.add(i + j)
            grandTotal -= i + j
            print i + j

print grandTotal