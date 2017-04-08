#!/usr/bin/env python

import fileinput

num_matrix = []
size_row = 0
size_col = 0

# imports file and maps it as a 2-D matrix of ints

for line in fileinput.input():
	# line = line.replace('\n', '').split(' ')
	size_row += 1
	line = map(int, line.split(' '))
	if size_col == 0:
		size_col = len(line)
	num_matrix.append(line)

# check to make sure file input is read correctly
# print num_matrix
# print "Matrix is " + str(size_row) + " by " + str(size_col)

# compares 4 numbers and returns the biggest
def cmp_ext(a, b, c, d, e):
	big = a
	if cmp(big, b) < 0:
		big = b
	if cmp(big, c) < 0:
		big = c
	if cmp(big, d) < 0:
		big = d
	if cmp(big, e) < 0:
		big = e
	return big

biggest_num = 0
adj = 4 # how many adjacent numbers to check + 1

for j in range(size_row):
	for i in range(size_col):
		x_prod = 1
		y_prod = 1
		xydr_prod = 1
		xydl_prod = 1
		#product going across
		if i <= (size_col - adj):
			for m in range(adj):
				x_prod *= num_matrix[j][i + m]
		#product going down
		if j <= (size_row - adj):
			for m in range(adj):
				y_prod *= num_matrix[j + m][i]
		#product going diagonal down right
		if (i <= (size_col - adj)) and (j <= (size_row - adj)):
			for m in range(adj):
				xydr_prod *= num_matrix[j + m][i + m]
		if (i >= (adj - 1)) and (j <= (size_row - adj)):
			for m in range(adj):
				xydl_prod *= num_matrix[j + m][i - m]
		#debugging
		# print "Coordinates: " + "(" + str(i) + ", " + str(j) + ")"
		# print "x_prod: " + str(x_prod)
		# print "y_prod: " + str(y_prod)
		# print "xy_prod: " + str(xy_prod)
		# print "current biggest num: " + str(biggest_num)

		biggest_num = cmp_ext(biggest_num, x_prod, y_prod, xydr_prod, xydl_prod)

print biggest_num