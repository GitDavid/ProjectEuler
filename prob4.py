def is_pal(num):
	""" Takes int and returns True if palindrome; else false"""
	num_arr = list(str(num))
	num_len = len(num_arr)
	for i in range(num_len):
		if num_arr[i] != num_arr[num_len - i - 1]:
			return False
	return True

def big_pal(dig):
	"""Finds largest palindrome that can be found 
	as a product of 2 numbers with n digit long"""
	low = 10 ** (dig - 1)
	high = 10 ** dig
	biggest = 0
	for i in range(low, high):
		for j in range(low, high):
			if (i * j > biggest) and is_pal(i * j):
				biggest = i * j
	return biggest