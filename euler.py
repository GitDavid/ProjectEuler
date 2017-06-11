'''
library created for commonly used Project Euler problems
'''

def is_prime(x):
    '''
    returns True if x is prime; False if not
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

def primes_up_to(x):
    '''
    returns list of all primes up to (excluding) x
    '''
    primes_list = []
    for i in range(x - 1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list
