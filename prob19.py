from datetime import date

'''
We will time travel and keep count of every first that is a Sunday
'''

current = date(1901, 1, 1)
Sundays = 0

while not ((current.year == 2000) and (current.month == 12)):
	if current.isoweekday() == 7:
		Sundays += 1
	if current.month != 12:
		current = current.replace(month = current.month + 1)
	else:
		current = current.replace(year = current.year + 1, month = 1)
	print "Year: " + str(current.year) + " Month: " + str(current.month) + " DofW: " + str(current.isoweekday())
	# print current.year
	# print current.month

print Sundays