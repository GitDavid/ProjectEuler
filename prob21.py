def pDivisors(n):
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    return arr

def sumArr(arr):
    total = 0
    for i in arr:
        total += i
    return total

def d(n):
    '''sum of proper divisors less than n'''
    return sumArr(pDivisors(n))

def amicable(a, b):
    return d(a) == b and d(b) == a and a != b

high = 10000
probset = range(1, high)
sum_am_num = 0

for i in probset:
    if amicable(i, d(i)) and i < high and d(i) < high:
        print i, d(i)
        sum_am_num += i + d(i)
        probset.remove(i)
        probset.remove(d(i))

print sum_am_num
