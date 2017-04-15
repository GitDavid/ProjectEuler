#!/usr/bin/env python

import fileinput

sum = 0

# imports file and maps it as a 2-D matrix of ints

for line in fileinput.input():
	# line = line.replace('\n', '').split(' ')
	sum += int(line)

sum_str = str(sum)

print sum_str[:10]