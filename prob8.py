#!/usr/bin/env python

'''
Executed with file as argv
Removes newlines
Evaluates product of 13 consecutive digits, and prints largest
'''

import fileinput

bignum = ""

for line in fileinput.input():
	bignum += line

num = bignum.replace('\n', '')

bigprod = 0

for i in range(len(num) - 13):
	prod = 1
	for i in range(i, i + 13):
		prod *= int(num[i])
	if prod > bigprod:
		bigprod = prod

print bigprod