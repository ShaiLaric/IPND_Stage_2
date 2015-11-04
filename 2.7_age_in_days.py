# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def isLeapYear(year):
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm

    if not year % 4 == 0:
    	return False
    elif not year % 100 == 0:
    		return True
    elif not year % 400 == 0:
    		return False
    else:
    	return True


#print isLeapYear(2000)
#print isLeapYear(2003)
#print isLeapYear(2006)
#print isLeapYear(2012)
#print isLeapYear(2014)


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	oneYear = 365									# constant (not accurate, not a float)
	daysInBirthMonth = daysOfMonths[m1 - 1]
	daysToEndOfBirthMonth = daysInBirthMonth - d1
	monthsToEndOfBirthYear = 12 - m1				# probably useless
	birthYearDayCount = 0	 						# do I need this?
	birthYearMonthCount = 0
	while birthYearMonthCount <= m1 - 2:
		birthYearDayCount += daysOfMonths[birthYearMonthCount]
		birthYearMonthCount += 1
		# print "birthYearMonthCount == " + str(birthYearMonthCount)
		# print "birthYearDayCount == " + str(birthYearDayCount)
	birthYearDayCount = birthYearDayCount + d1
	# print "birthYearDayCount == " + str(birthYearDayCount)
	daysLeftInBirthYear = oneYear - birthYearDayCount
	print "daysLeftInBirthYear == " + str(daysLeftInBirthYear)
# 	all this is useless without figuring in leap years!
#
#	interveningYears = y2 - y1 - 1
#	interveningYearDays = oneYear * interveningYears
#	print "interveningYears == " + str(interveningYears) + "; which means that interveningYearDays == " + str(interveningYearDays)
	yearList = [y1]
	counter = y1
	while counter < y2:
		yearList.append(counter + 1)
		counter += 1
#	print yearList
	dayCounter = 0
	for e in yearList:
		if isLeapYear(e):
			dayCounter +=366
		else:
			dayCounter +=365
	print "Days between 1/1/" + str(y1) + " and 12/31/" + str(y2) + ": " + str(dayCounter) + ", inclusive."
	dayCounter = dayCounter - daysLeftInBirthYear
	print "Days between 1/1/" + str(y1) + " and " + str(m2) + "/" + str(d2) + "/" + str(y2) + ": " + str(dayCounter) + ", inclusive."
	thisYearDayCount = 0	 						# do I need this?
	thisYearMonthCount = m2 - 1
	while thisYearMonthCount <= m2 and thisYearMonthCount !=0:
		thisYearDayCount += daysOfMonths[thisYearMonthCount]
		thisYearMonthCount -= 1
		# print "thisYearMonthCount == " + str(thisYearMonthCount)
	thisYearDayCount += d2 + 1
	print "thisYearDayCount == " + str(thisYearDayCount)
	days = dayCounter - thisYearDayCount
    	return days


print daysBetweenDates(1972, 11, 24, 2015, 11, 4)
print daysBetweenDates(1972, 11, 24, 1972, 11, 28)
