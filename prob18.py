#!/usr/bin/env python

# imports triangle as 2-D matrix and maps all numbers to ints

import fileinput

num_matrix = []

for line in fileinput.input():
	line = map(int, line.split(' '))
	num_matrix.append(line)
	print line

# calculates the sum of each path and returns the largest

'''
implementing pure brute force algo
'''

def dec_to_bin(x):
	'''
	converts a decimal int to binary string
	'''
	if x == 0: return "0"
	bin = ""
	i = 0
	while 2 ** i <= x:
		i += 1
	i -= 1
	while i >= 0:
		if 2 ** i <= x:
		  bin += "1"
		  x -= 2 ** i
		else:
		  bin += "0"
		i -= 1
	return bin

def generatePath(rows, n):
	'''
	Given a triangle with rows, 
	n is nth path given there are total n paths
	Each path is mapped to a binary str, 0 = left, 1 = right
	returns an array with length of rows representing the path
	'''
	binpath = dec_to_bin(n)
	while len(binpath) < rows - 1:
		binpath = "0" + binpath
	count = 0
	path = []
	for i in range(len(binpath)):
		if binpath[i] == "1":
			count += 1
		path.append(count)
	path.insert(0, 0)
	return path

def find_max(triangle):
	'''
	takes a triangle and finds the max by calculating 
	the length of all paths
	'''
	rows = len(triangle)
	longest = 0
	x = []

	for i in range(2 ** rows):
		x = generatePath(rows, i)
		sum = 0
		for y in range(rows):
			sum += triangle[y][x[y]]
		if sum > longest:
			longest = sum
	return longest

print find_max(num_matrix)

'''
implementing memoize/recursion from
http://stackoverflow.com/questions/20303553/max-path-triangle-python
memoize is not necessary for this problem
'''
# def memoize(func):
# 	memo = {}
# 	def wrapper(*args):
# 		if args in memo:
# 			return memo[args]
# 		else:
# 			rv = func(*args)
# 			memo[args] = rv
# 			return rv
# 	return wrapper

# @memoize
# def getmaxofsub(x, y):
# 	if y == len(num_matrix) or x > y: return 0
# 	return num_matrix[y][x] + max(getmaxofsub(x, y + 1), \
# 		getmaxofsub(x + 1, y + 1))

# print getmaxofsub(0, 0)