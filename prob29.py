distinct_terms = set()

def distinct_powers(a, b):
	global distinct_terms
	for i in range(2, a + 1):
		for j in range(2, b + 1):
			distinct_terms.add(i ** j)

distinct_powers(100, 100)

print(len(distinct_terms))