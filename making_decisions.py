# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

#print 2 < 3			# True
#print 21 < 3		# False
#print 7 * 3 < 21	# False
#print 7 * 3 != 21	# False
#print 7 * 3 == 21	# True

# The above are comparison operators.

#if 7 > 3:
#	print "7 is bigger than 3."

#def absolute(x):
#	if x < 0:
#		x = -x
#	return x
#
#print absolute(0)

def bigger(a, b):
	if a > b:
		r = a
	else:
		r = b
	return r

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

def is_friend(name):
	if name[0] == "D" or name[0] == "N":
		return True
	else:
		return False

print is_friend("Diane")
print is_friend("Ned")
print is_friend("Arry")

def biggest(a, b, c):
	if a > b:
		if a > c:
			return a
		if b > c:
			return b
		else:
			return c

print biggest(3, 6, 9)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)
