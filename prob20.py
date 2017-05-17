from math import factorial

def sumDig(x):
    '''
    sums up the digits in a number
    '''
    x = factorial(x)
    arrx = list(str(x))
    sum = 0
    for i in range(len(arrx)):
        sum += int(arrx[i])
    return sum
