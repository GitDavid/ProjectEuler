import math

'''
library created for commonly used Project Euler problems
'''

def is_prime(x):
    '''
    returns True if x is prime; False if not
    basic checks for lower numbers and all primes = 6k +/-1
    '''
    if x == 1 or x == 0:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    elif x < 9:
        return True
    else:
        r = math.floor(math.sqrt(x))
        f = 5
        while f <= r:
            if (x % f == 0) or (x % (f + 2) == 0):
                return False
            f += 6
        return True

def primes_up_to(x):
    '''
    returns list of all primes up to (excluding) x
    '''
    primes_list = []
    for i in range(x - 1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list
