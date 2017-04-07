def is_pytrip(a, b, c):
	'''checks for pythagorean triplet'''
	if (a ** 2) + (b ** 2) == (c **2):
		return True
	else:
		return False


'''iterates through all combinations of i and j to find
py triplet that sums to 1000'''

i = 1
found = False

while i < 1000:
	j = 1
	while j < 1000:
		k = 1000 - i - j
		# print "running: " + str(i) + ", " + str(j) + ", " + str(k)
		if (is_pytrip(i, j, k) and (i + j + k == 1000)):
			print "Solution is: " + str(i) + ", " + str(j) + ", " + str(k)
			found = True
			break
		j += 1
	if found == True:
		break
	i += 1

print i * j * k