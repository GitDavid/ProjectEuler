#!/usr/bin/env python

import fileinput

sum = ""

for line in fileinput.input():
	# line = line.replace('\n', '').split(' ')
	sum += line

sum = sum.replace("\"", "")
sum = sum.split(",")
sum.sort()

def nameScore(name):
	score = 0
	for i in name:
		score += ord(i) - 64 #since A = 65
	return score

total = 0

for i in sum:
	total += (sum.index(i) + 1) * nameScore(i)

print total
