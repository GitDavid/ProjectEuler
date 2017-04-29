ones = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine"
}

teens = {
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen"
}

tens = {
	2: "twenty",
	3: "thirty",
	4: "forty",
	5: "fifty",
	6: "sixty",
	7: "seventy",
	8: "eighty",
	9: "ninety",
}

def ntow(x):
	'''takes an int and returns the (brit) english word str'''
	word = ""
	ones_place = x % 10
	tens_place = x  / 10 % 10
	hundreds_place = x / 100 % 10
	thousands_place = x / 1000 % 10

	if thousands_place > 0:
		word += "onethousand"
	if hundreds_place > 0:
		word += ones[hundreds_place] + "hundred"
	if (thousands_place > 0 or hundreds_place) and \
	 (tens_place > 0 or ones_place > 0):
		word += "and"
	if tens_place == 1:
		word += teens[x % 100]
	elif tens_place > 1:
		word += tens[tens_place]
		if ones_place > 0:
			word += ones[ones_place]
	elif ones_place > 0:
		word += ones[ones_place]

	return word

COUNT = 0

for i in range(1, 1001):
	COUNT += len(ntow(i))

print COUNT